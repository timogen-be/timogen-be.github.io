<template>
  <div>
    <!-- Patho Location -->
    <h5>Lieu de prestation</h5>
    <br />
    <div class="form-check" v-for="(types, location) in pathos" :key="location" @change="emitAll">
      <input
        class="form-check-input"
        type="radio"
        :value="location"
        v-model="selected_location"
      />
      {{ location }}
    </div>
    <br />
    <br />

    <!-- Patho Type -->
    <h5>Type de pathologie</h5>
    <br />
    <div v-for="(types, location) in pathos" :key="location" @change="emitAll">
      <div v-show="location == selected_location" class="form-check">
        <div v-for="(type, type_id) in types" :key="type_id">
          <input
            class="form-check-input"
            type="radio"
            :value="type"
            v-model="selected_patho"
          />
          {{ type }}
        </div>
      </div>
    </div>
    <br />
    <br />

    <h5>Options Supplémentaires</h5>
    <br />
    <!-- DLM -->
    <div class="form-check form-switch">
      <input
        class="form-check-input"
        type="checkbox"
        id="flexSwitchCheckDefault"
      />
      <label class="form-check-label" for="flexSwitchCheckDefault"
        >Drainage Lympatique manuel</label
      >
    </div>
    <br />
  </div>
</template>

<script>
export default {
  name: "Patho",
  created() {
    this.emitAll();
  },
  components: {},
  data() {
    return {
      selected_patho: "Courantes",
      selected_location:
        "cabinet du kinésithérapeute, situé en dehors d'un hôpital",
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
  props: {},
  methods: {
    emitAll() {
        this.$emit('receive', this.selected_location, this.selected_patho);
    }
  },
};
</script>

<style></style>
