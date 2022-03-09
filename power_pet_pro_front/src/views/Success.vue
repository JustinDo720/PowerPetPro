<template>
  <div class="page-success">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Thank you</h1>
        <p>
          Your order will be processed by our agents within the next 2 days.
        </p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Success",

  mounted() {
    // We are just setting the title of the documents
    document.title = "Success | Pet Power Pro";
  },
};
</script>
