<template>
  <div class="mb-3 d-flex flex-wrap">
    <label class="col-12 col-sm-4 col-md-3 col-lg-2 col-form-label">
      {{ label }}
    </label>
    <div class="col">
      <slot></slot>
    </div>
  <br />
  <br />
  </div>
</template>

<script>
export default {
  name: "LabelizedField",
  components: {},
  props: {
    label: String,
  },
  methods: {},
};
</script>
