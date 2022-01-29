<template>
  <div>
    <!-- Patient Name -->
    <LabelizedField for="patient_name" label="Nom du patient">
      <input
        id="patient_name"
        name="patient_name"
        type="patient_name"
        class="form-control"
        placeholder="NOM Prénom"
        v-model="patient_name"
      />
    </LabelizedField>

    <!-- Patient NISS -->
    <LabelizedField for="patient_niss" label="NISS">
      <input
        id="patient_niss"
        name="patient_niss"
        type="niss"
        class="form-control"
        placeholder="00.01.01-000.01"
        v-model="patient_niss"
        maxlength="15"
      />
    </LabelizedField>

    <!-- Patient Address -->
    <LabelizedField for="patient_address" label="Adresse">
      <textarea
        id="patient_address"
        name="patient_address"
        rows="2"
        cols="50"
        maxlength="200"
        type="address"
        class="form-control"
        v-model="patient_address"
      />
    </LabelizedField>

    <!-- special tarif -->
    <LabelizedField for="special_tarif" label="Tarif préférentiel">
      <div class="form-check form-switch">
        <input
          class="form-check-input"
          type="checkbox"
          v-model="patient_special_tarif"
          id="special_tarif"
        />
      </div>
    </LabelizedField>

    <!-- Mutuality Name -->
    <LabelizedField for="mutuality_name" label="Mutuelle">
      <input
        id="mutuality_name"
        name="mutuality_name"
        type="mutuality_name"
        class="form-control"
        v-model="mutuality_name"
      />
    </LabelizedField>

    <!-- Mutuality Address -->
    <LabelizedField for="mutuality_address" label="Adresse de la mutuelle">
      <textarea
        id="mutuality_address"
        name="mutuality_address"
        rows="2"
        cols="50"
        maxlength="200"
        type="address"
        class="form-control"
        v-model="mutuality_address"
      />
    </LabelizedField>
  </div>
</template>

<script>
import LabelizedField from "./Label.vue";
import { mapGetters, mapMutations } from "vuex";

export default {
  name: "Patient",
  components: {
    LabelizedField,
  },
  data() {
    return {};
  },
  methods: {
    ...mapMutations("patient", [
      "setPatientName",
      "setPatientNiss",
      "setPatientAddress",
      "setPatientSpecialTarif",
      "setMutualityName",
      "setMutualityAddress",
    ]),
  },
  computed: {
    ...mapGetters("patient", [
      "getPatientName",
      "getPatientNiss",
      "getPatientAddress",
      "getPatientSpecialTarif",
      "getMutualityName",
      "getMutualityAddress",
    ]),
    patient_name: {
      get() {
        return this.getPatientName;
      },
      set(new_value) {
        return this.setPatientName(new_value);
      },
    },
    patient_niss: {
      get() {
        return this.getPatientNiss;
      },
      set(new_value) {
        return this.setPatientNiss(new_value);
      },
    },
    patient_address: {
      get() {
        return this.getPatientAddress;
      },
      set(new_value) {
        return this.setPatientAddress(new_value);
      },
    },
    patient_special_tarif: {
      get() {
        return this.getPatientSpecialTarif;
      },
      set(new_value) {
        return this.setPatientSpecialTarif(new_value);
      },
    },
    mutuality_name: {
      get() {
        return this.getMutualityName;
      },
      set(new_value) {
        return this.setMutualityName(new_value);
      },
    },
    mutuality_address: {
      get() {
        return this.getMutualityAddress;
      },
      set(new_value) {
        return this.setMutualityAddress(new_value);
      },
    },
  },
};
</script>

<style></style>
