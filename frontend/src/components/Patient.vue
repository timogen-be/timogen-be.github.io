<template>
  <div>
    <!-- Patient Name -->
    <label for="patient_name" class="form-label">Nom:</label>

    <input
      id="patient_name"
      name="patient_name"
      type="patient_name"
      class="form-control"
      placeholder="NOM Prénom"
    />
    <br />

    <!-- Patient NISS -->
    <label for="patient_niss" class="form-label">NISS</label>

    <input
      id="patient_niss"
      name="patient_niss"
      type="niss"
      class="form-control"
      placeholder="95.05.27-007.42"
    />
    <br />

    <!-- Patient Address -->
    <label for="patient_address" class="form-label">Adresse postale</label>

    <textarea
      id="patient_address"
      name="patient_address"
      rows="2"
      cols="50"
      maxlength="200"
      type="address"
      class="form-control"
      placeholder=""
    />
    <br />
  </div>
</template>

<script>
export default {
  name: "Thearpist",
  components: {},
  data() {
    return {
    };
  },
  props: {
    msg: String,
  },
  methods: {
  },
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
