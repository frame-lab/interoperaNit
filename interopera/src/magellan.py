import py_entitymatching as em
import random


class Magellan:
    def __init__(self) -> None:
        self.base_path = 'train/base.csv'
        self.matched_base_path = 'train/matched_base.csv'
        self.labeled_base_path = 'train/labeled_base.csv'

    @staticmethod
    def get_match_params(base, matched_base):
        return [parameter for parameter in base.match_parameters
                if parameter['name'] == matched_base.name]

    def generate_csvs(self, base, matched_base, match_params):
        base_file = open(self.base_path, 'w', encoding='utf-8')
        matched_base_file = open(self.matched_base_path, 'w', encoding='utf-8')
        labeled_base_file = open(self.labeled_base_path, 'w', encoding='utf-8')

        random_table_size = min(len(base.entities),
                                len(matched_base.entities))

        base_file.write('index')
        matched_base_file.write('index')
        labeled_base_file.write('_id,ltable_index,rtable_index')

        base_param_indexes = []
        matched_param_indexes = []

        base_parameters = []
        matched_parameters = []

        for match_param in match_params:
            base_parameter = match_param["my_parameter"]
            matched_base_parameter = match_param["matched_parameter"]

            base_param_indexes.append(
                base.parameters.index(base_parameter))
            matched_param_indexes.append(
                matched_base.parameters.index(matched_base_parameter))

            base_parameters.append(base_parameter["parameter"])
            matched_parameters.append(matched_base_parameter["parameter"])

        for parameter in base_parameters:
            labeled_base_file.write(f',ltable_{parameter}')
            base_file.write(f',{parameter}')

        for parameter in matched_parameters:
            labeled_base_file.write(f',rtable_{parameter}')
            matched_base_file.write(f',{parameter}')

        labeled_base_file.write(f',gold')

        for entity_index in range(0, len(base.entities)):
            base_file.write(f'\n{entity_index}')
            for param_index in base_param_indexes:
                base_file.write(f',{base.entities[entity_index][param_index]}')

        for entity_index in range(0, len(matched_base.entities)):
            matched_base_file.write(f'\n{entity_index}')
            for param_index in matched_param_indexes:
                matched_base_file.write(
                    f',{matched_base.entities[entity_index][param_index]}')

        for entity_index in range(0, random_table_size):
            labeled_base_file.write(
                f'\n{entity_index},{entity_index},{entity_index}')
            for param_index in base_param_indexes:
                labeled_base_file.write(
                    f',{base.entities[entity_index][param_index]}')
            for param_index in matched_param_indexes:
                labeled_base_file.write(
                    f',{matched_base.entities[entity_index][param_index]}')
            labeled_base_file.write(f',{random.randint(0, 1)}')

        base_file.close()
        matched_base_file.close()
        labeled_base_file.close()

    def make_predict(self, match_params):
        base_csv = em.read_csv_metadata(self.base_path, key='index')
        matched_base_csv = em.read_csv_metadata(
            self.matched_base_path, key='index')

        ob = em.OverlapBlocker()

        blocked_tables = ob.block_tables(
            base_csv,
            matched_base_csv,
            match_params[0]['my_parameter']['parameter'],
            match_params[0]['matched_parameter']['parameter'],
            l_output_attrs=[
                param['my_parameter']['parameter'] for param in match_params],
            r_output_attrs=[
                param['matched_parameter']['parameter'] for param in match_params],
            overlap_size=len(match_params))

        label_table = em.read_csv_metadata(
            self.labeled_base_path,
            key='_id',
            ltable=base_csv,
            rtable=matched_base_csv,
            fk_ltable='ltable_index',
            fk_rtable='rtable_index')

        feature_table = em.get_features_for_matching(
            base_csv, matched_base_csv, validate_inferred_attr_types=False)

        ltable = [
            f'ltable_{param["my_parameter"]["parameter"]}' for param in match_params]

        rtable = [
            f'rtable_{param["matched_parameter"]["parameter"]}' for param in match_params]

        attrs_from_table = ltable + rtable

        test_vecs_table = em.extract_feature_vecs(
            label_table,
            feature_table=feature_table,
            attrs_before=attrs_from_table,
            attrs_after='gold',
            n_jobs=-1)

        rf = em.RFMatcher()

        test_attrs_to_be_excluded = []
        test_attrs_to_be_excluded.extend(
            ['_id', 'ltable_index', 'rtable_index', 'gold'])
        test_attrs_to_be_excluded.extend(attrs_from_table)
        
        rf.fit(
            table=test_vecs_table,
            exclude_attrs=test_attrs_to_be_excluded,
            target_attr='gold')

        predictions = rf.predict(
            table=test_vecs_table,
            exclude_attrs=test_attrs_to_be_excluded,
            append=True,
            target_attr='predicted',
            inplace=False)
            
        predictions.head()

    def align(self, base, matched_base):
        match_params = self.get_match_params(base, matched_base)
        self.generate_csvs(base, matched_base, match_params)
        self.make_predict(match_params)
