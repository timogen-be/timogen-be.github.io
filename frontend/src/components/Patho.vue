<template>
  <div>
    <h4>Lieu de prestation</h4>
    <!-- Patho Location -->
    <div class="form-check" v-for="(types, location, id) in pathos" :key="location">
      <input
        class="form-check-input"
        type="radio"
        :value="id"
        v-model="selected_location"
      />
      {{ location }}
    </div>
    <br />

    <!-- Patho Type -->
    <h4>Type de pathologie</h4>
    <div v-for="(types, location, id) in pathos" :key="id">
      <div v-show="id == selected_location" class="form-check">
        <div v-for="(type, type_id) in types" :key="type_id">
          <input
            class="form-check-input"
            type="radio"
            :value="type_id"
            v-model="selected_patho"
          />
          {{ type }}
        </div>
      </div>
    </div>
    <br>

    <!-- ID première séance -->
    Commence à la séance

  </div>
</template>

<script>
export default {
  name: "Patho",
  components: {},
  data() {
    return {
      selected_patho: 0,
      selected_location: 0,
      pathos: {
        "cabinet du kinésithérapeute, situé en dehors d'un hôpital": [
          "Courantes",
          "Lourdes (§ 11)",
          "Soins intensifs / Néonatalogie (§ 12)",
          "Périnatalité (§ 13)",
          "FA (§ 14)",
          "FB (§ 14)",
        ],
        "cabinet du kinésithérapeute, situé dans un hôpital": [
          "Courantes",
          "Lourdes (§ 11)",
          "Soins intensifs / Néonatalogie (§ 12)",
          "Périnatalité (§ 13)",
        ],
        domiciles: [
          "Courantes",
          "Lourdes (§ 11)",
          "Soins intensifs / Néonatalogie (§ 12)",
          "Périnatalité (§ 13)",
          "FA (§ 14)",
          "FB (§ 14)",
          "Patients palliatifs",
        ],
        "personnes handicapées ou résidents": [
          "Courantes",
          "Lourdes (§ 11)",
          "Soins intensifs / Néonatalogie (§ 12)",
          "Périnatalité (§ 13)",
          "FA (§ 14)",
          "FB (§ 14)",
        ],
        "maison de soins psychiatrique": [
          "Courantes",
          "Lourdes (§ 11)",
          "Soins intensifs / Néonatalogie (§ 12)",
          "Périnatalité (§ 13)",
          "FA (§ 14)",
          "FB (§ 14)",
        ],
        hospitalisés: [
          "Courantes",
          "Lourdes (§ 11)",
          "Soins intensifs / Néonatalogie (§ 12)",
          "Périnatalité (§ 13)",
        ],
        "centres de rééducation fonctionnelle conventionnés": [
          "Courantes",
          "Lourdes (§ 11)",
          "Soins intensifs / Néonatalogie (§ 12)",
          "Périnatalité (§ 13)",
          "FA (§ 14)",
          "FB (§ 14)",
        ],
        "personnes âgées": [
          "Courantes",
          "Lourdes (§ 11)",
          "Soins intensifs / Néonatalogie (§ 12)",
          "FA (§ 14)",
          "FB (§ 14)",
        ],
        "hôpital de jour": [
          'Article 7, § 1, 8°: prestations effectuées à un bénéficiaire admis en "Hôpital de jour"',
        ],
      },
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
