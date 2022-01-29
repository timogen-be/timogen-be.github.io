import Vue from 'vue'
import Vuex from 'vuex'
import { createLogger } from 'vuex'

import therapist from './modules/therapist'
import patient from './modules/patient'
import patho from './modules/patho'
import seances from './modules/seances'
// import ads from './modules/ads'

const debug = process.env.NODE_ENV !== 'production'

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    therapist,
    patient,
    patho,
    seances,
    // ads,
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
