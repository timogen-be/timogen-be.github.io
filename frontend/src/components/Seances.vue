<template>
  <div>
    <!-- ID première séance -->
    <div class="form-outline" v-on="emitSeances">
      <label class="form-label" for="seance_number"
        >Commencer à la séance:</label
      >
      <input
        type="number"
        id="seance_number"
        class="form-control-inline"
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
        v-on:click="increaseCounter"
        type="button"
        class="col-md-3 col-sm-6 btn btn-primary"
      >
        Ajouter une ADS
      </button>
      <button
        v-if="count"
        v-on:click="decreaseCounter"
        type="button"
        class="col-md-3 col-sm-6 btn btn-danger"
      >
        supprimer une ADS
      </button>
    </div>

  </div>
</template>

<script>
import ADS from "./ADS.vue";

export default {
  name: "Seances",
  components: {
    ADS,
  },
  data() {
    return {
      first_seance: 1,
      count: 0,
      dates: []
    };
  },
  props: {},
  methods: {
    decreaseCounter() {
      this.count--;
      if (this.count < 0) {
        this.count = 0;
      }
      this.dates.slice(0, this.count + 1);
    },
    increaseCounter() {
      this.count++;
      this.dates.push({});
    },
    emitSeances() {
      this.$emit("receive", this.first_seance, this.dates);
    },
    receiveDate(index, new_dates) {
      // Splice to change the size of the main array so the 
      // changes are directly taken into account.
      this.dates.splice(index-1, 1);
      this.dates.splice(index-1, 0, new_dates);
      this.emitSeances();
    }
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
