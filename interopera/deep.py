import deepmatcher as dm

model = dm.MatchingModel()
train, validation, test = dm.data.process(
    path='train',
    train='train.csv',
    validation='valid.csv',
    test='test.csv')
model.run_train(
    train,
    validation,
    best_save_path='best_model.pth')
model.run_eval(test)
