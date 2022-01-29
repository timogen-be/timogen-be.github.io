// initial state
const state = () => ({
  address: "",
  bank_account: "",
  bce: "",
  contracted: false,
  id: 0,
  inami_nb: "",
  name: ""
})

// getters
const getters = {
  getTherapist: state => {
    return state;
  },
  getName: state => {
    return state.name;
  },
  getAddress: state => {
    return state.address;
  },
  getInamiNb: state => {
    return state.inami_nb;
  },
  getBce: state => {
    return state.bce;
  },
  getBankAccount: state => {
    return state.bank_account;
  },
  getContracted: state => {
    return state.contracted;
  },
}

// actions
const actions = {
}

// mutations - setters
const mutations = {
  setTherapist(state, therapist) {
    if (therapist) {
      state.address = therapist.address;
      state.bank_account = therapist.bank_account;
      state.bce = therapist.bce;
      state.contracted = therapist.contracted;
      state.id = therapist.id;
      state.inami_nb = therapist.inami_nb;
      state.name = therapist.name;
    } else {
      state.address = "";
      state.bank_account = "";
      state.bce = "";
      state.contracted = false;
      state.id = 0;
      state.inami_nb = "";
      state.name = "";
    }
  },
  setAddress(state, value) {
    state.address = value;
  },
  setInamiNb(state, value) {
    var new_inami = ""
    for (let index = 0; index < value.length; index++) {
      // place the dots
      if (new_inami.length == 1 || new_inami.length == 9) {
        if (value[index] != '-') {
          new_inami += '-';
        }
      }
      if (value[index] >= '0' && value[index] <= '9') {
        new_inami += value[index];
      }
    }
    state.inami_nb = new_inami;
  },
  setBce(state, value) {
    var new_bce = ""
    for (let index = 0; index < value.length; index++) {
      // place the dots
      if (new_bce.length == 4 || new_bce.length == 8) {
        if (value[index] != '.') {
          new_bce += '.';
        }
      }
      if (value[index] >= '0' && value[index] <= '9') {
        new_bce += value[index];
      }
    }
    state.bce = new_bce;
  },
  setBankAccount(state, value) {
    var new_ba = "";
    value = value.replace(/\s/g, '');
    for (let index = 0; index < value.length; index++) {
      // place the spaces
      if (index % 4 === 0 && index > 0) {
        new_ba += ' ';
      }
      new_ba += value[index];
    }
    state.bank_account = new_ba.toUpperCase();
  },
  setContracted(state, value) {
    state.contracted = value;
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
