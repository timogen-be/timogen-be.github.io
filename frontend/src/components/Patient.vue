<template>
  <div>
    <!-- Patient Name -->
    <LabelizedField for="patient_name" label="Nom du patient" v-on="$emit('receive', 'patient', 'mutuality')">
      <input
        id="patient_name"
        name="patient_name"
        type="patient_name"
        class="form-control"
        placeholder="NOM Prénom"
        v-model="patient.name"
      />
    </LabelizedField>

    <!-- Patient NISS -->
    <LabelizedField for="patient_niss" label="NISS" v-on="$emit('receive', 'patient', 'mutuality')">
      <input
        id="patient_niss"
        name="patient_niss"
        type="niss"
        class="form-control"
        placeholder="95.05.27-007.42"
        v-model="patient.niss"
      />
    </LabelizedField>

    <!-- Patient Address -->
    <LabelizedField for="patient_address" label="addresse" v-on="$emit('receive', 'patient', 'mutuality')">
      <textarea
        id="patient_address"
        name="patient_address"
        rows="2"
        cols="50"
        maxlength="200"
        type="address"
        class="form-control"
        v-model="patient.address"
      />
    </LabelizedField>

    <!-- Mutuality Name -->
    <LabelizedField for="mutuality_name" label="Mutuelle" v-on="$emit('receive', 'patient', 'mutuality')">
      <input
        id="mutuality_name"
        name="mutuality_name"
        type="mutuality_name"
        class="form-control"
        v-model="mutuality.name"
      />
    </LabelizedField>

    <!-- Mutuality Address -->
    <LabelizedField for="mutuality_address" label="addresse de la mutuelle" v-on="$emit('receive', 'patient', 'mutuality')">
      <textarea
        id="mutuality_address"
        name="mutuality_address"
        rows="2"
        cols="50"
        maxlength="200"
        type="address"
        class="form-control"
        v-model="mutuality.address"
      />
    </LabelizedField>
  </div>
</template>

<script>
import LabelizedField from "./Label.vue";

export default {
  name: "Patient",
  components: {
    LabelizedField,
  },
  data() {
    return {
    };
  },
  props: ['patient', 'mutuality'],
  methods: {},
};
</script>

<style>
.autocomplete__icon {
  display: none;
}

.autocomplete__inputs {
  padding: 0px !important;
}

.autocomplete__box {
  padding: 0px !important;
}
</style>
