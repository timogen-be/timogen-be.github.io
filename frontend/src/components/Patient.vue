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
      />
    </LabelizedField>

    <!-- Patient NISS -->
    <LabelizedField for="patient_niss" label="NISS">
      <input
        id="patient_niss"
        name="patient_niss"
        type="niss"
        class="form-control"
        placeholder="95.05.27-007.42"
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
        placeholder
      />
    </LabelizedField>

    <!-- Mutuality Name -->
    <LabelizedField for="mutuality_name" label="Mutuelle">
      <input
        id="mutuality_name"
        name="mutuality_name"
        type="mutuality_name"
        class="form-control"
        placeholder
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
        placeholder
      />
    </LabelizedField>
  </div>
</template>

<script>
import LabelizedField from "./Label.vue";

export default {
  name: "Thearpist",
  components: {
    LabelizedField,
  },
  data() {
    return {};
  },
  props: {
    msg: String,
  },
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
