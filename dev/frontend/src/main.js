import Vue from 'vue'
import App from './App.vue'
// import VueCookies from "vue-cookies";
import store from "./store";
import Autocomplete from 'v-autocomplete'
import 'v-autocomplete/dist/v-autocomplete.css'
import VueHtml2Canvas from 'vue-html2canvas';
 
Vue.use(VueHtml2Canvas);

Vue.config.productionTip = false

// Vue.use(VueCookies);

const app = new Vue({
  render: h => h(App),
  store,
  Autocomplete
})

app.$mount('#app')
