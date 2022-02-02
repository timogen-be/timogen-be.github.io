<template>
  <div>
    <!-- ID première séance -->
    <div class="form-outline">
      <label class="form-label" for="seance_number"
        >Commencer à la séance:</label
      >
      <input
        id="seance_number"
        class="form-control-inline"
        type="number"
        v-model="first_seance"
      />
    </div>
    <br />

    <div v-for="n in count" :key="n">
      <hr />
      <br />
      <ADS @receive="receiveDate" :index="n"></ADS>
    </div>

    <div class="d-flex justify-content-between">
      <button
        class="col-md-3 col-sm-6 btn btn-success"
        type="button"
        v-on:click="incrementCount"
      >
        Ajouter une ADS
      </button>
      <button
        class="col-md-3 col-sm-6 btn btn-danger"
        type="button"
        v-if="count"
        v-on:click="decrementCount"
      >
        supprimer une ADS
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex"
import ADS from "./ADS.vue"

export default {
  name: "Seances",
  components: {
    ADS,
  },
  computed: {
    ...mapGetters("seances", ["getFirstSeance", "getAdsList", "getCount"]),
    count: {
      get() {
        return this.getCount
      },
    },
    first_seance: {
      get() {
        return this.getFirstSeance
      },
      set(new_value) {
        return this.setFirstSeance(new_value)
      },
    },
    ads_list: {
      get() {
        return this.getAdsList
      },
      set(new_value) {
        return this.setAdsList(new_value)
      },
    },
  },
  methods: {
    ...mapMutations("seances", ["setFirstSeance", "setAdsList", "addAds"]),
    ...mapActions("seances", ["incrementCount", "decrementCount"]),
    receiveDate(index, new_dates) {
      // Splice to change the size of the main array so the
      // changes are directly taken into account.
      new_dates.index = index
      this.addAds(new_dates)
    },
  },
};
</script>

<style>
#seance_number {
  margin-left: 10px;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  max-width: 45px;
}
</style>
