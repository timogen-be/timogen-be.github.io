// initial state
const state = () => ({
  patient_name: "",
  patient_niss: "",
  patient_address: "",
  patient_special_tarif: true,
  mutuality_name: "",
  mutuality_address: "",
})

// getters
const getters = {
  getPatientName: state => {
    return state.patient_name;
  },
  getPatientNiss: state => {
    return state.patient_niss;
  },
  getPatientAddress: state => {
    return state.patient_address;
  },
  getPatientSpecialTarif: state => {
    return state.patient_special_tarif;
  },
  getMutualityName: state => {
    return state.mutuality_name;
  },
  getMutualityAddress: state => {
    return state.mutuality_address;
  },
}

// actions
const actions = {
}

// mutations - setters
const mutations = {
  setPatientName(state, value) {
    state.patient_name = value;
  },
  setPatientNiss(state, value) {
    var new_niss = ""
    for (let index = 0; index < value.length; index++) {
      if (new_niss.length == 2 || new_niss.length == 5 || new_niss.length == 11) {
        if (value[index] != '.') {
          new_niss += '.';
        }
      }
      if (new_niss.length == 8) {
        if (value[index] != '-') {
          new_niss += '-';
        }
      }
      if (value[index] >= '0' && value[index] <= '9') {
        new_niss += value[index];
      }
    }
    state.patient_niss = new_niss;
  },
  setPatientAddress(state, value) {
    state.patient_address = value;
  },
  setPatientSpecialTarif(state, value) {
    state.patient_special_tarif = value;
  },
  setMutualityName(state, value) {
    state.mutuality_name = value;
  },
  setMutualityAddress(state, value) {
    state.mutuality_address = value;
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
