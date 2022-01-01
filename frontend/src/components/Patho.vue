<template>
  <div>
    <!-- Patho Type -->
      <div class="form-check" v-for="pt in pathos_types" v-bind:key="pt.value">
        <input class="form-check-input" type="radio" name="text" :value="pt.value" v-model=selected />
{{pt.text}}
      </div>
    <br />
  </div>
</template>

<script>
export default {
  name: "Patho",
  components: {},
  data() {
    return {
      selected: 2,
      pathos_types: [
        {
          text: 'Article 7, \u00a7 1, 8\u00b0: prestations effectu\u00e9es \u00e0 un b\u00e9n\u00e9ficiaire admis en "H\u00f4pital de jour"',
          value: "1",
        },
        { text: "Courantes", value: "2" },
        { text: "FA (\u00a7 14)", value: "3" },
        { text: "FB (\u00a7 14)", value: "4" },
        {
          text: "Indemnit\u00e9 pour les frais de d\u00e9placement du kin\u00e9sith\u00e9rapeute",
          value: "5",
        },
        { text: "Lourdes (\u00a7 11)", value: "6" },
        { text: "P\u00e9rinatalit\u00e9 (\u00a7 13)", value: "7" },
        { text: "Patients palliatifs", value: "8" },
        { text: "Soins intensifs / N\u00e9onatalogie (\u00a7 12)", value: "9" },
      ],
    };
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
