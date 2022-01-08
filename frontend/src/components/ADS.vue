<template>
  <div>
    <div class="form-inline d-flex align-items-center justify-content-center" v-on:change="emitDate">
      <label for="ads_number"> Numéro d'ADS </label>
      <input
        id="ads_number"
        name="ads_number"
        type="number"
        class="form-control-inline"
        placeholder="Numéro d'ADS"
        v-model="ads_number"
      />
    </div>
    <br />
    <div class="d-flex justify-content-center" v-on:change="emitDate">
      <vc-calendar
        ref="calendar"
        :attributes="attributes"
        @dayclick="onDayClick"
        locale="fr"
        :columns="$screens({ default: 1, md: 2, lg: 3 })"
        v-model="dates"
      />
      </div>
      <br>
      <br>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import VCalendar from "v-calendar";
import LabelizedField from "./Label.vue";

// Use v-calendar & v-date-picker components
Vue.use(VCalendar, {
  componentPrefix: "vc",
});

export default {
  name: "ADS",
  data() {
    return {
      ads_number: false,
      days: [],
    };
  },
  props: ['index'],
  computed: {
    LabelizedField,
    dates() {
      return this.days.map((day) => day.date);
    },
    attributes() {
      return this.dates.map((date) => ({
        highlight: true,
        dates: date,
      }));
    },
  },
  methods: {
    onDayClick(day) {
      const idx = this.days.findIndex((d) => d.id === day.id);
      if (idx >= 0) {
        this.days.splice(idx, 1);
      } else {
        this.days.push({
          id: day.id,
          date: day.date,
        });
      }
      this.emitDate();
    },
    emitDate()  {
      let new_dates = {
        days: this.days.map((day) => day.id),
        ads_number: this.ads_number,
      }
      this.$emit('receive', this.index, new_dates);
    }
  },
};
</script>

<style>
#ads_number {
  margin-left: 8px;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  max-width: 300px;
}
</style>
