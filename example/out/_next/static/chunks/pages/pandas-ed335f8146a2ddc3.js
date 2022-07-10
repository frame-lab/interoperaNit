(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[318],{7068:function(e,t,n){"use strict";n.d(t,{Z:function(){return l}});n(7294);var r=n(2125),i={default:(0,r.iv)(["border-radius:30px;background-color:",";"],(function(e){return e.theme.palette.primary.blue})),image:(0,r.iv)(["background-color:transparent;"])},o={small:(0,r.iv)(["border:none;width:30px;height:30px;",";"],(function(e){return e.variant&&i[e.variant]})),large:(0,r.iv)(["border:none;height:50px;width:",";",";"],(function(e){return e.width}),(function(e){return e.variant&&i[e.variant]}))},a=r.ZP.button.withConfig({displayName:"styles__Button",componentId:"sc-uynfsy-0"})(["",";",";outline:none;cursor:pointer;font-weight:",";font-size:",";font-family:",";color:",";text-decoration:",";margin:",";"],(function(e){return o[e.size]}),(function(e){return e.disabled&&(0,r.iv)(["background:#7e8190;cursor:not-allowed;"])}),(function(e){return e.theme.typography.button.fontWeight}),(function(e){return e.theme.typography.button.fontSize}),(function(e){return e.theme.typography.button.fontFamily}),(function(e){return e.color||e.theme.palette.primary.white}),(function(e){return e.textDecoration||e.theme.typography.button.textDecoration}),(function(e){return e.margin})),c=n(5893);function s(e){var t=e.children,n=e.variant,r=e.onClick,i=e.disabled,o=e.type,s=e.size,l=e.color,u=e.textDecoration,d=e.margin,f=e.width;return(0,c.jsx)(a,{variant:n,onClick:r,disabled:i,type:o,size:s,color:l,textDecoration:u,margin:d,width:f,children:t})}s.defaultProps={children:"",onClick:function(){},size:"small",variant:"default",disabled:!1,type:"button",color:"",textDecoration:"",margin:"0",width:"auto"};var l=s},8299:function(e,t,n){"use strict";n.d(t,{Z:function(){return a}});n(7294);var r=n(2125).ZP.div.withConfig({displayName:"styles__Image",componentId:"sc-oqh2tu-0"})(["width:",";height:",";max-height:",";background-image:url(",");background-repeat:",";background-color:",";background-position:",";background-size:",";filter:",";"],(function(e){return e.width}),(function(e){return e.height}),(function(e){return e.maxHeight}),(function(e){return e.image}),(function(e){return e.repeat}),(function(e){return e.color}),(function(e){return e.position}),(function(e){return e.size}),(function(e){return e.filter})),i=n(5893);function o(e){var t=e.image,n=e.width,o=e.height,a=e.maxHeight,c=e.repeat,s=e.color,l=e.position,u=e.size,d=e.filter,f=e.alt;return(0,i.jsx)(r,{alt:f,image:t,width:n,height:o,maxHeight:a,repeat:c,color:s,position:l,size:u,filter:d})}o.defaultProps={width:"100%",height:"100%",repeat:"no-repeat",color:"transparent",position:"center",size:"auto",filter:"",maxHeight:"none"};var a=o},6553:function(e,t,n){"use strict";n.d(t,{Z:function(){return b}});var r=n(6687),i=(n(7294),n(2125)),o=i.ZP.div.withConfig({displayName:"styles__Container",componentId:"sc-16hyffj-0"})(["display:flex;flex-direction:column;height:480px;width:70%;margin-top:30px;align-items:center;margin-bottom:30px;"]),a=i.ZP.div.withConfig({displayName:"styles__HorizontalContainer",componentId:"sc-16hyffj-1"})(["display:flex;flex-direction:row;margin-top:30px;"]),c=i.ZP.button.withConfig({displayName:"styles__DragArea",componentId:"sc-16hyffj-2"})(["display:flex;flex-direction:column;height:400px;width:70%;border:5px dashed white;border-radius:50px;align-items:center;justify-content:center;"]),s=i.ZP.div.withConfig({displayName:"styles__VerticalContainer",componentId:"sc-16hyffj-3"})(["display:flex;flex-direction:column;margin-top:30px;margin-left:50px;"]),l=i.ZP.div.withConfig({displayName:"styles__Scroll",componentId:"sc-16hyffj-4"})(["display:flex;flex-direction:column;height:300px;overflow-y:scroll;::-webkit-scrollbar{width:10px;}::-webkit-scrollbar-track{box-shadow:inset 0 0 5px grey;border-radius:10px;}::-webkit-scrollbar-thumb{background:grey;border-radius:10px;}border:5px solid white;border-radius:20px;"]),u=n(5263),d=i.ZP.div.withConfig({displayName:"styles__Container",componentId:"sc-mwr3h5-0"})(["display:flex;flex-direction:row;padding:10px;align-items:center;justify-content:center;border-bottom:5px solid white;"]),f=i.ZP.div.withConfig({displayName:"styles__VerticalContainer",componentId:"sc-mwr3h5-1"})(["display:flex;flex-direction:column;width:80px;"]),p=n(7068),h=n(8299),g=n(5893);var x=function(e){var t=e.file,n=e.removeFile,r="".concat("/interoperaNit","/remove.svg"),i="".concat("/interoperaNit","/file.svg");return(0,g.jsxs)(d,{children:[(0,g.jsxs)(f,{children:[(0,g.jsx)(h.Z,{image:i,width:"50px",height:"50px",size:"cover",alt:"file"}),(0,g.jsx)(u.Z,{fontSize:"20px",width:"110px",variant:"body1",whiteSpace:"nowrap",textOverflow:"ellipsis",overflow:"hidden",margin:"10px 100px 0 0",children:t.name})]}),(0,g.jsx)(p.Z,{size:"small",variant:"image",onClick:n,children:(0,g.jsx)(h.Z,{alt:"remove",image:r,filter:"brightness(0) invert(1)",width:"30px",height:"30px",size:"cover"})})]})},m=n(125);function y(e){var t=e.files,n=e.setFiles,i=e.text,d=e.maxFiles,f="".concat("/interoperaNit","/download.svg");return(0,g.jsxs)(o,{children:[(0,g.jsx)(u.Z,{fontSize:"30px",width:"auto",tAlign:"center",variant:"h1",children:"Files"}),(0,g.jsxs)(a,{children:[(0,g.jsxs)(c,{onClick:function(){(!d||t.length<d)&&n([].concat((0,r.Z)(t),[{name:"test"}]))},children:[(0,g.jsx)(h.Z,{image:f,width:"150px",height:"150px",size:"cover",alt:"download"}),(0,g.jsx)(u.Z,{lineHeight:"120%",fontSize:"30px",width:"65%",tAlign:"center",variant:"h1",children:i})]}),(0,g.jsxs)(s,{children:[(0,g.jsx)(u.Z,{margin:"0 0 20px 0",fontSize:"20px",width:"150px",tAlign:"center",variant:"h1",children:"File input"}),(0,g.jsx)(l,{children:t.map((function(e,r){var i="fileItem_".concat(r);return(0,g.jsx)(x,{file:e,removeFile:function(){return(0,m.JW)(t,n,r)}},i)}))})]})]})]})}y.defaultProps={maxFiles:0};var b=y},8649:function(e,t,n){"use strict";n.d(t,{Z:function(){return a}});n(7294);var r=n(5263),i=n(2125).ZP.div.withConfig({displayName:"styles__Body",componentId:"sc-1s6x2c7-0"})(["display:flex;flex-direction:column;height:500px;width:100%;margin-top:30px;justify-content:center;align-items:center;"]),o=n(5893);var a=function(e){var t=e.processType;return(0,o.jsx)(i,{children:(0,o.jsxs)(r.Z,{fontSize:"35px",variant:"h1",children:["Realizing the ",function(){switch(t){case"alignment":return"alignment";case"dm":return"deep matcher";case"pandas":return"query";default:return""}}()," process"]})})}},96:function(e,t,n){"use strict";n.d(t,{Z:function(){return m}});n(7294);var r=n(2125),i=r.ZP.div.withConfig({displayName:"styles__Container",componentId:"sc-i0r9wc-0"})(["display:flex;flex-direction:column;height:500px;width:70%;margin-top:30px;"]),o=r.ZP.div.withConfig({displayName:"styles__Scroll",componentId:"sc-i0r9wc-1"})(["display:flex;flex-direction:column;overflow-y:auto;::-webkit-scrollbar{width:10px;}::-webkit-scrollbar-track{box-shadow:inset 0 0 5px grey;border-radius:10px;}::-webkit-scrollbar-thumb{background:grey;border-radius:10px;}"]),a=r.ZP.div.withConfig({displayName:"styles__HorizontalContainer",componentId:"sc-i0r9wc-2"})(["display:flex;flex-direction:row;margin-top:20px;justify-content:space-around;align-items:center;"]),c=n(9499),s=r.ZP.textarea.withConfig({displayName:"styles__Textarea",componentId:"sc-668jll-0"})(["padding:0.5em;color:",";background:",";border:",";border-radius:",";width:",";height:",";justify-content:center;align-items:center;resize:none;outline:none;::-webkit-scrollbar{width:10px;}::-webkit-scrollbar-track{box-shadow:inset 0 0 5px grey;border-radius:10px;}::-webkit-scrollbar-thumb{background:grey;border-radius:10px;}"],(function(e){return e.color}),(function(e){return e.background}),(function(e){return e.border}),(function(e){return e.borderRadius}),(function(e){return e.width}),(function(e){return e.height})),l=n(5893);function u(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function d(e,t){var n=e.type,r=e.value,i=e.color,o=e.background,a=e.border,d=e.borderRadius,f=e.width,p=e.height,h=e.onChange;return(0,l.jsx)(s,function(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?u(Object(n),!0).forEach((function(t){(0,c.Z)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):u(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}({type:n,value:r,color:i,background:o,border:a,borderRadius:d,width:f,height:p,onChange:h},t))}d.defaultProps={type:"text",color:"black",background:"white",border:"transparent",borderRadius:"5px",width:"80%",height:"100px",props:{}};var f=d,p=n(7068),h=n(8299),g=n(5263),x=n(125);var m=function(e){var t=e.queries,n=e.setQueries,r=t.length-1;return(0,l.jsxs)(i,{children:[(0,l.jsx)(g.Z,{fontSize:"30px",width:"auto",tAlign:"center",variant:"h1",children:"Queries"}),(0,l.jsx)(o,{children:t.map((function(e,i){var o=r===i,c=o?"add.svg":"remove.svg",s="".concat("/interoperaNit","/").concat(c),u=o?function(){return(0,x.mm)(t,n,"")}:function(){return(0,x.JW)(t,n,i)},d="query_".concat(i);return(0,l.jsxs)(a,{children:[(0,l.jsx)(f,{value:e,onChange:function(e){return(0,x.RI)(t,n,e.target.value,i)}}),(0,l.jsx)(p.Z,{size:"small",variant:"image",onClick:u,children:(0,l.jsx)(h.Z,{alt:"button",image:s,filter:"brightness(0) invert(1)",width:"30px",height:"30px",size:"cover"})})]},d)}))})]})}},7572:function(e,t,n){"use strict";n.r(t),n.d(t,{default:function(){return m}});var r=n(9499),i=n(7294),o=n(1163),a=n(5263),c=n(6553),s=n(7068),l=n(8649),u=n(96),d=n(9141),f=n(2125).ZP.div.withConfig({displayName:"styles__Body",componentId:"sc-n5ly6h-0"})(["display:flex;flex-direction:column;height:100%;width:100%;justify-content:center;align-items:center;margin-bottom:20px;margin-top:20px;"]),p=n(5893);function h(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function g(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?h(Object(n),!0).forEach((function(t){(0,r.Z)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):h(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var x=function(){var e=(0,o.useRouter)(),t=(0,i.useState)(1),n=t[0],r=t[1],h=(0,i.useState)([]),x=h[0],m=h[1],y=(0,i.useState)([""]),b=y[0],w=y[1],v="pandas",j=function(){switch(n){case 1:x.length&&r(2);break;case 2:r(3);var t=(0,d.N)({files:x,queries:b,processType:v});setTimeout((function(){e.push({pathname:"".concat("/interoperaNit","/finished"),query:g({},t)},"finished")}),5e3)}};return(0,p.jsxs)(f,{children:[(0,p.jsxs)(a.Z,{fontSize:"35px",variant:"h1",children:["Step ",n,"/3"]}),function(){switch(n){case 1:return(0,p.jsx)(c.Z,{files:x,setFiles:m,text:"Drag 'n' drop one file here, or click to select a file\n(Only one *.csv file will be accepted)",maxFiles:1});case 2:return(0,p.jsx)(u.Z,{queries:b,setQueries:w});case 3:return(0,p.jsx)(l.Z,{processType:v});default:return null}}(),3!==n?(0,p.jsx)(s.Z,{onClick:j,size:"large",variant:"default",width:"200px",children:(0,p.jsx)(a.Z,{fontSize:"20px",width:"auto",variant:"h1",tAlign:"center",children:"CONFIRM"})}):null]})};function m(){return(0,p.jsx)(x,{})}},125:function(e,t,n){"use strict";n.d(t,{JW:function(){return o},RI:function(){return a},mm:function(){return i}});var r=n(6687);function i(e,t,n){t([].concat((0,r.Z)(e),[n]))}function o(e,t,n){var i=(0,r.Z)(e);i.splice(n,1),t(i)}function a(e,t,n,i){var o=(0,r.Z)(e);o[i]=n,t(o)}},9141:function(e,t,n){"use strict";function r(e){for(var t in e)e[t]=JSON.stringify(e[t]);return e}n.d(t,{N:function(){return r}})},6296:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/pandas",function(){return n(7572)}])},1163:function(e,t,n){e.exports=n(9898)},6687:function(e,t,n){"use strict";function r(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,r=new Array(t);n<t;n++)r[n]=e[n];return r}function i(e){return function(e){if(Array.isArray(e))return r(e)}(e)||function(e){if("undefined"!==typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(e)||function(e,t){if(e){if("string"===typeof e)return r(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);return"Object"===n&&e.constructor&&(n=e.constructor.name),"Map"===n||"Set"===n?Array.from(e):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?r(e,t):void 0}}(e)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}n.d(t,{Z:function(){return i}})}},function(e){e.O(0,[774,888,179],(function(){return t=6296,e(e.s=t);var t}));var t=e.O();_N_E=t}]);