<template>
  <div>
    <!-- Patho Location -->
    <h5>Lieu de prestation</h5>
    <br />
    <div class="form-check" v-for="location in locations" :key="location.id">
      <input
        class="form-check-input"
        type="radio"
        :value="location"
        v-model="selected_location"
      />
      {{ location.name }}
    </div>
    <br />
    <br />

    <!-- Patho -->
    <h5>Pathologie</h5>
    <br />
    <div class="form-check" v-for="patho in pathos" :key="patho.name + 1000">
      <input
        class="form-check-input"
        type="radio"
        :value="patho"
        v-model="selected_patho"
      />
      {{ patho.name }}
    </div>
    <br />
    <br />

    <!-- Seance Kinds -->
    <div v-if="kinds.length >= 2">
      <h5>Type des séances</h5>
      <br />
      <div class="form-check" v-for="kind in kinds" :key="kind">
        <input
          class="form-check-input"
          type="radio"
          :value="kind"
          v-model="selected_kind"
        />
        {{ kind }}
      </div>
      <br />
      <br />
    </div>

    <!-- Seance Kinds -->
    <div v-if="times.length >= 2">
      <h5>Durée des séances</h5>
      <br />
      <div class="form-check" v-for="time in times" :key="time">
        <input
          class="form-check-input"
          type="radio"
          :value="time"
          v-model="selected_time"
        />
        {{ time }}
      </div>
      <br />
      <br />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";

export default {
  name: "Patho",
  created() {
    this.$store.dispatch("patho/getAllLocations");
  },
  components: {},
  props: {},
  methods: {
    ...mapMutations("patho", [
      "setSelectedLocation",
      "setSelectedPatho",
      "setSelectedKind",
      "setSelectedTime",
    ]),
  },
  computed: {
    ...mapGetters("patho", [
      "getSelectedLocation",
      "getSelectedPatho",
      "getSelectedKind",
      "getSelectedTime",
      "getLocations",
      "getPathos",
      "getKinds",
      "getTimes",
    ]),
    locations: {
      get() {
        return this.getLocations;
      },
    },
    pathos: {
      get() {
        return this.getPathos;
      },
    },
    kinds: {
      get() {
        return this.getKinds;
      },
    },
    times: {
      get() {
        return this.getTimes;
      },
    },
    selected_location: {
      get() {
        return this.getSelectedLocation;
      },
      set(new_value) {
        return this.setSelectedLocation(new_value);
      },
    },
    selected_patho: {
      get() {
        return this.getSelectedPatho;
      },
      set(new_value) {
        return this.setSelectedPatho(new_value);
      },
    },
    selected_kind: {
      get() {
        return this.getSelectedKind;
      },
      set(new_value) {
        return this.setSelectedKind(new_value);
      },
    },
    selected_time: {
      get() {
        return this.getSelectedTime;
      },
      set(new_value) {
        return this.setSelectedTime(new_value);
      },
    },
  },
};

</script>

<style></style>
