// initial state
const state = () => ({
    id: 0,
    number: "",
    dates: []
})

// getters
const getters = {
    getNumber: state => { return state.number; },
    getDates: state => { return state.dates; },
}

// setters
const mutations = {
    setNumber(state, value) { state.number = value; },
    setDates(state, value) { state.dates = value; },
    clickDate(state, value) {
        const idx = state.dates.findIndex((d) => d.id === value.id);
        if (idx >= 0) {
            state.dates.splice(idx, 1);
        } else {
            state.dates = [value.id, ...state.dates].sort();
        }

    }
}

// actions
const actions = {
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
