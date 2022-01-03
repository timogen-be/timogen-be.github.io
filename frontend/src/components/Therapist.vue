<template>
  <!-- Therapist -->
  <div>
    <!-- name -->
    <!-- TODO: allow custom input -->
    <LabelizedField for="therapist_name" label="Nom">
      <autocomplete
        id="therapist_name"
        class="col-sm"
        ref="therapist"
        placeholder="commencez à écrire..."
        input-class="form-control"
        results-property="results"
        :source="therapistsEndpoint"
        :results-display="name"
        :showNoResults="false"
        @selected="addTherapist"
      >
      </autocomplete>
    </LabelizedField>

    <!-- Address -->
    <LabelizedField for="therapist_address" label="Adresse">
      <textarea
        id="therapist_address"
        name="therapist_address"
        rows="2"
        cols="50"
        maxlength="200"
        type="address"
        class="form-control"
        placeholder=""
        v-model="therapist.adress"
      />
    </LabelizedField>

    <!-- inami -->
    <LabelizedField for="therapist_inami" label="Numéro INAMI">
      <input
        id="therapist_inami"
        name="therapist_inami"
        type="inami"
        class="form-control"
        placeholder="0-0000000-000"
        v-model="therapist.inami_nb"
      />
    </LabelizedField>

    <!-- BCE -->
    <LabelizedField for="therapist_bce" label="BCE">
      <input
        id="therapist_bce"
        name="therapist_bce"
        type="bce"
        class="form-control"
        placeholder="0000.000.000"
        v-model="therapist.bce"
      />
    </LabelizedField>

    <!-- Bank -->
    <LabelizedField for="therapist_ba" label="Numéro de compte">
      <input
        id="therapist_ba"
        name="therapist_ba"
        type="bank_account"
        class="form-control"
        placeholder="BE40 0000 0000 0000"
        v-model="therapist.bank_account"
      />
    </LabelizedField>

    <!-- contracted -->
    <div class="form-check">
      <input
        class="form-check-input"
        type="checkbox"
        v-model="therapist.contracted"
        id="defaultCheck1"
      />
      <label class="form-check-label" for="defaultCheck1"> Conventionné </label>
      <br />
      <br />
    </div>
  </div>
</template>

<script>
import Autocomplete from "vuejs-auto-complete";
import LabelizedField from "./Label.vue";

export default {
  name: "Thearpist",
  components: {
    Autocomplete,
    LabelizedField,
  },
  data() {
    return {
      therapist: {
        adress: "",
        bank_account: "",
        bce: "",
        contracted: false,
        id: 0,
        inami_nb: "",
        name: "",
      },
    };
  },
  props: {
    msg: String,
  },
  methods: {
    therapistsEndpoint(input) {
      return "http://127.0.0.1:8000/api/therapist/?therapist=" + input;
    },
    addTherapist(therapist) {
      this.therapist = therapist.selectedObject;
      // access the autocomplete component methods from the parent
      // this.$refs.autocomplete.clear();
    },
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
