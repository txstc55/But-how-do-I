(function(){"use strict";var t={8154:function(t,e,o){var n=o(9242),s=o(3396);function i(t,e){const o=(0,s.up)("router-view");return(0,s.wg)(),(0,s.j4)(o,null,{default:(0,s.w5)((({Component:t})=>[(0,s.Wm)(n.uT,{name:"fade"},{default:(0,s.w5)((()=>[((0,s.wg)(),(0,s.j4)((0,s.LL)(t)))])),_:2},1024)])),_:1})}var r=o(89);const a={},l=(0,r.Z)(a,[["render",i]]);var d=l,c=o(678),u=o(7139);const g=(0,s._)("div",{class:"h-screen w-screen -z-10"},null,-1),h=(0,s._)("div",{class:"-z-10",style:{height:"50vh"}},null,-1),p=(0,s._)("div",{class:"mt-1 mb-4 text-gray-400 w-full text-center z-50"},[(0,s.Uk)(" A collection of code snippets by "),(0,s._)("a",{target:"_blank",href:"https://txstc55.github.io/",class:"underline italic z-50"},"Xuan Tang"),(0,s.Uk)(" from his side projects"),(0,s._)("br"),(0,s.Uk)("Suggestions? Email me: txstc55[at]gmail[dot]com ")],-1);function m(t,e,o,n,i,r){const a=(0,s.up)("TitleComponent"),l=(0,s.up)("PostGridView");return(0,s.wg)(),(0,s.iD)("div",null,[g,(0,s._)("div",{class:"fixed top-0 h-screen w-screen main-title -z-10",style:(0,u.j5)({filter:"blur("+this.blur+"px)",opacity:this.opacity})},[(0,s.Wm)(a)],4),h,(0,s.Wm)(l),p])}const f=t=>((0,s.dD)("data-v-70b67119"),t=t(),(0,s.Cn)(),t),v={class:"h-screen font-mono no-select titleText -z-10"},x=f((()=>(0,s._)("div",{class:"h-1/2 relative -z-10"},[(0,s._)("div",{class:"absolute bottom-0 text-2xl pl-8 pb-5"},"I have a CS degree")],-1))),w={class:"h-1/2 relative -z-10"},b={class:"text-5xl m-auto pl-5 absolute top-1/5 sm:text-6xl md:text-7xl lg:text-8xl xl:text-9xl"};function y(t,e,o,n,i,r){return(0,s.wg)(),(0,s.iD)("div",v,[x,(0,s._)("div",w,[(0,s._)("div",b," BUT HOW DO I "+(0,u.zw)(i.dots),1)])])}var S={name:"TitleComponent",data(){return{dots:".   ",dotCount:1}},methods:{},created(){let t=this;setInterval((()=>{t.dotCount=(t.dotCount+1)%4,t.dots=".".repeat(t.dotCount)+" ".repeat(4-t.dotCount)}),600)}};const C=(0,r.Z)(S,[["render",y],["__scopeId","data-v-70b67119"]]);var T=C;const _=t=>((0,s.dD)("data-v-18b150a2"),t=t(),(0,s.Cn)(),t),k={class:"board min-h-screen relative"},O=_((()=>(0,s._)("div",{class:"text-2xl font-mono my-14 mx-auto text-center sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl text-white no-select"}," THINGS I FIND USEFUL ",-1))),P={class:"items-center mb-8 text-center no-select"},D=["onClick","disabled"],H={key:0,class:"text-white sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl no-select text-center my-auto pt-20 font-mono"},j={class:"items-center mb-1 mt-10 text-center bottom-1 absolute left-1/2 -translate-x-1/2 no-select"},I=["onClick"];function z(t,e,o,n,i,r){const a=(0,s.up)("PostGridComponent");return(0,s.wg)(),(0,s.iD)("div",k,[O,(0,s._)("div",P,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(i.tagsSorted,(t=>((0,s.wg)(),(0,s.iD)("button",{class:(0,u.C_)(["border-2 rounded-lg px-2 py-1 mx-2 w-fit shadow-lg inline-block mb-2 text-xs sm:text-xs md:text-sm lg:text-lg xl:text-lg hover:bg-white hover:text-black hover:scale-110 hover:shadow-2xl active:bg-gray-900 active:text-gray-200 disabled:hover:border-gray-500 disabled:text-gray-500 disabled:hover:scale-100 disabled:transition-none disabled:hover:shadow-none disabled:hover:bg-inherit active:scale-100 active:shadow-lg transition duration-300 whitespace-pre font-mono",-1!=i.tagsSelected.indexOf(t.name)?"text-white border-white":"text-gray-400 border-gray-500"]),key:t.name,onClick:e=>r.selectTag(t.name),disabled:0==t.count},(0,u.zw)(t.name+"  "+t.count),11,D)))),128))]),0==i.postsSelected.length?((0,s.wg)(),(0,s.iD)("div",H," NO POST FOUND ")):(0,s.kq)("",!0),((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(i.postsSelected.slice((i.page-1)*i.postPerPage,Math.min(i.postsSelected.length,i.page*i.postPerPage)),(t=>((0,s.wg)(),(0,s.j4)(a,{key:t.id,title:t.title,tags:t.tags},null,8,["title","tags"])))),128)),(0,s._)("div",j,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(Math.ceil(i.postsSelected.length/i.postPerPage),(t=>((0,s.wg)(),(0,s.iD)("button",{class:(0,u.C_)(["rounded-md px-2 mx-2 w-fit shadow-lg inline-block mb-2 text-xs sm:text-xs md:text-sm lg:text-lg xl:text-lg transition duration-300 whitespace-pre bg-gray-500/20 font-mono hover:bg-gray-200/20",i.page==t?"border-2 border-white text-white":"border-2 border-none text-white/80"]),key:t,onClick:e=>r.changePage(t)},(0,u.zw)(t),11,I)))),128))])])}const M={class:"w-4/5 mx-auto shadow-inner mb-5 hover:shadow-2xl animate-all transition hover:scale-102 border-gray-900 border-2 rounded-lg duration-200 hover:border-gray-900/30 post-grid"},U={class:"text-white text-xl sm:text-xl md:text-2xl lg:text-3xl xl:text-3xl break-words px-5 py-7 font-mono"};function E(t,e,o,n,i,r){const a=(0,s.up)("router-link"),l=(0,s.up)("TagComponent");return(0,s.wg)(),(0,s.iD)("div",M,[(0,s._)("div",U,[(0,s.Wm)(a,{to:"/post/"+o.title,class:"no-select"},{default:(0,s.w5)((()=>[(0,s.Uk)((0,u.zw)(o.title),1)])),_:1},8,["to"])]),(0,s.Wm)(l,{tags:o.tags},null,8,["tags"])])}var L=o(5179),A={name:"PostGridComponent",props:{title:String,tags:Array},components:{TagComponent:L.Z}};const Z=(0,r.Z)(A,[["render",E],["__scopeId","data-v-81ea38ae"]]);var F=Z,N=JSON.parse('[{"title":"How Do I Print to Console With Color in c++","tags":["c++","c","command line"],"id":0},{"title":"How Do I Access History in Zsh","tags":["zsh","command line"],"id":1},{"title":"How Do I Execute a Function After a Command in Zsh","tags":["zsh","command line"],"id":2},{"title":"How Do I Check if a Command Exists in Command Line","tags":["command line"],"id":3},{"title":"How Do I Use CORS","tags":["nodejs","javascript"],"id":4},{"title":"How Do I Create a 3D Box Using HTML","tags":["html","css"],"id":5},{"title":"How Do I Have a Function That Reads Unknown Number of Arguments in c++","tags":["c++"],"id":6},{"title":"How Do I Use Google Translate for Free in My Web Project","tags":["javascript"],"id":7},{"title":"How Do I Use range() Function in Languages Other Than Python","tags":["javascript","vuejs","c++"],"id":8},{"title":"How Do I Draw Triangle Using HTML and CSS","tags":["html","css"],"id":9},{"title":"How Do I Draw a Sphere Using Only HTML and CSS","tags":["html","css"],"id":10}]'),B={name:"PostGridView",components:{PostGridComponent:F},data(){return{posts:[],tagsToPosts:{},tagsSorted:[],tagsSortedOriginal:[],tagsSelected:[],postsSelected:[],page:1,postPerPage:4}},methods:{changePage(t){this.page=t},selectTag(t){this.page=1;var e=!0;const o=this.tagsSelected.indexOf(t);if(o>-1?(this.tagsSelected.splice(o,1),e=!1):this.tagsSelected.push(t),0==this.tagsSelected.length){this.postsSelected=this.posts;for(var n=0;n<this.tagsSorted.length;n++)this.tagsSorted[n].count=this.tagsSortedOriginal[n].count}else{let o=this;if(e){var s={};this.postsSelected=this.postsSelected.filter((e=>{const o=e.tags.indexOf(t);if(-1==o){for(var n=0;n<e.tags.length;n++){const t=e.tags[n];t in s?s[t]+=1:s[t]=1}return!1}return!0}));for(n=0;n<o.tagsSorted.length;n++){const t=o.tagsSorted[n].name;t in s&&(o.tagsSorted[n].count-=s[t])}}else{let t=this;var i={};this.postsSelected=this.posts.filter((e=>{for(var o=0;o<t.tagsSelected.length;o++)if(-1==e.tags.indexOf(t.tagsSelected[o]))return!1;for(o=0;o<e.tags.length;o++){const t=e.tags[o];t in i?i[t]+=1:i[t]=1}return!0}));for(n=0;n<this.tagsSorted.length;n++){const t=this.tagsSorted[n].name;this.tagsSorted[n].count=t in i?i[t]:0}}}}},created(){if(0==this.posts.length){this.posts=N.sort((function(t,e){return t.id-e.id})),this.posts=this.posts.reverse(),this.postsSelected=this.posts;for(var t=0;t<this.posts.length;t++)for(var e=0;e<this.posts[t].tags.length;e++){var o=this.posts[t].tags[e];o in this.tagsToPosts?this.tagsToPosts[o].push(this.posts[t].id):this.tagsToPosts[o]=[this.posts[t].id]}}for(var o in this.tagsToPosts)this.tagsSorted.push({name:o,count:this.tagsToPosts[o].length});this.tagsSorted.sort((function(t,e){return e.count-t.count}));for(t=0;t<this.tagsSorted.length;t++)this.tagsSortedOriginal.push({name:this.tagsSorted[t].name,count:this.tagsSorted[t].count})}};const G=(0,r.Z)(B,[["render",z],["__scopeId","data-v-18b150a2"]]);var W=G,Y={name:"HomeView",components:{TitleComponent:T,PostGridView:W},data(){return{blur:0,opacity:1}},methods:{computeBlurAndOpacity(){this.blur=Math.min(15,Math.ceil(window.scrollY/(.7*window.innerHeight)*15)),this.opacity=Math.max(0,1.5-window.scrollY/(.7*window.innerHeight))},scrollMethod(){this.computeBlurAndOpacity()},resizeMethod(){this.computeBlurAndOpacity()}},created(){setTimeout((()=>{window.scrollTo(0,0)}),510),window.addEventListener("scroll",this.scrollMethod),window.addEventListener("resize",this.resizeMethod)},destroyed(){window.removeEventListener("scroll",this.scrollMethod),window.removeEventListener("resize",this.resizeMethod)}};const K=(0,r.Z)(Y,[["render",m]]);var V=K;const q=[{path:"/",name:"home",component:V},{path:"/post/:title",name:"Post",component:()=>o.e(554).then(o.bind(o,9554))}],R=(0,c.p7)({history:(0,c.PO)("/But-how-do-I/"),routes:q});var J=R;(0,n.ri)(d).use(J).mount("#app")},5179:function(t,e,o){o.d(e,{Z:function(){return c}});var n=o(3396),s=o(7139);const i={class:"py-6 px-3 text-xs sm:text-xs md:text-sm lg:text-lg xl:text-lg no-select font-mono overflow-hidden"};function r(t,e,o,r,a,l){return(0,n.wg)(),(0,n.iD)("div",i,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(o.tags.sort(),(t=>((0,n.wg)(),(0,n.iD)("div",{class:"border-2 rounded-md px-3 py-1 mx-2 float-left text-white",key:t},(0,s.zw)(t),1)))),128))])}var a={name:"TagComponent",props:{tags:Array},data(){return{parsedTags:[]}},created(){this.parsedTags=[]}},l=o(89);const d=(0,l.Z)(a,[["render",r]]);var c=d}},e={};function o(n){var s=e[n];if(void 0!==s)return s.exports;var i=e[n]={exports:{}};return t[n](i,i.exports,o),i.exports}o.m=t,function(){var t=[];o.O=function(e,n,s,i){if(!n){var r=1/0;for(c=0;c<t.length;c++){n=t[c][0],s=t[c][1],i=t[c][2];for(var a=!0,l=0;l<n.length;l++)(!1&i||r>=i)&&Object.keys(o.O).every((function(t){return o.O[t](n[l])}))?n.splice(l--,1):(a=!1,i<r&&(r=i));if(a){t.splice(c--,1);var d=s();void 0!==d&&(e=d)}}return e}i=i||0;for(var c=t.length;c>0&&t[c-1][2]>i;c--)t[c]=t[c-1];t[c]=[n,s,i]}}(),function(){o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,{a:e}),e}}(),function(){o.d=function(t,e){for(var n in e)o.o(e,n)&&!o.o(t,n)&&Object.defineProperty(t,n,{enumerable:!0,get:e[n]})}}(),function(){o.f={},o.e=function(t){return Promise.all(Object.keys(o.f).reduce((function(e,n){return o.f[n](t,e),e}),[]))}}(),function(){o.u=function(t){return"js/"+t+".05577213.js"}}(),function(){o.miniCssF=function(t){}}(),function(){o.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)}}(),function(){var t={},e="but-how-do-i:";o.l=function(n,s,i,r){if(t[n])t[n].push(s);else{var a,l;if(void 0!==i)for(var d=document.getElementsByTagName("script"),c=0;c<d.length;c++){var u=d[c];if(u.getAttribute("src")==n||u.getAttribute("data-webpack")==e+i){a=u;break}}a||(l=!0,a=document.createElement("script"),a.charset="utf-8",a.timeout=120,o.nc&&a.setAttribute("nonce",o.nc),a.setAttribute("data-webpack",e+i),a.src=n),t[n]=[s];var g=function(e,o){a.onerror=a.onload=null,clearTimeout(h);var s=t[n];if(delete t[n],a.parentNode&&a.parentNode.removeChild(a),s&&s.forEach((function(t){return t(o)})),e)return e(o)},h=setTimeout(g.bind(null,void 0,{type:"timeout",target:a}),12e4);a.onerror=g.bind(null,a.onerror),a.onload=g.bind(null,a.onload),l&&document.head.appendChild(a)}}}(),function(){o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})}}(),function(){o.p="/But-how-do-I/"}(),function(){var t={143:0};o.f.j=function(e,n){var s=o.o(t,e)?t[e]:void 0;if(0!==s)if(s)n.push(s[2]);else{var i=new Promise((function(o,n){s=t[e]=[o,n]}));n.push(s[2]=i);var r=o.p+o.u(e),a=new Error,l=function(n){if(o.o(t,e)&&(s=t[e],0!==s&&(t[e]=void 0),s)){var i=n&&("load"===n.type?"missing":n.type),r=n&&n.target&&n.target.src;a.message="Loading chunk "+e+" failed.\n("+i+": "+r+")",a.name="ChunkLoadError",a.type=i,a.request=r,s[1](a)}};o.l(r,l,"chunk-"+e,e)}},o.O.j=function(e){return 0===t[e]};var e=function(e,n){var s,i,r=n[0],a=n[1],l=n[2],d=0;if(r.some((function(e){return 0!==t[e]}))){for(s in a)o.o(a,s)&&(o.m[s]=a[s]);if(l)var c=l(o)}for(e&&e(n);d<r.length;d++)i=r[d],o.o(t,i)&&t[i]&&t[i][0](),t[i]=0;return o.O(c)},n=self["webpackChunkbut_how_do_i"]=self["webpackChunkbut_how_do_i"]||[];n.forEach(e.bind(null,0)),n.push=e.bind(null,n.push.bind(n))}();var n=o.O(void 0,[998],(function(){return o(8154)}));n=o.O(n)})();
//# sourceMappingURL=app.46beabe7.js.map