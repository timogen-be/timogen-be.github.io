<template>
  <div>
    <!-- Mutuality Name -->
    <label for="mutuality_name" class="form-label">Nom:</label>

    <input
      id="mutuality_name"
      name="mutuality_name"
      type="mutuality_name"
      class="form-control"
      placeholder=""
    />
    <br />

    <!-- Mutuality Address -->
    <label for="mutuality_address" class="form-label">Adresse postale</label>

    <textarea
      id="mutuality_address"
      name="mutuality_address"
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
  name: "Mutuality",
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
