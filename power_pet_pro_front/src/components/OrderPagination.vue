<template>
  <nav class="pagination is-rounded" role="navigation" aria-label="pagination">
    <button
      class="pagination-previous"
      v-if="previous_page"
      @click="push_data(previous_page)"
    >
      Previous
    </button>
    <button
      class="pagination-next"
      v-if="next_page"
      @click="push_data(next_page)"
    >
      Next page
    </button>
  </nav>
</template>

<script>
import axios from "axios";
import Cookies from "cookies-js";

export default {
  name: "OrderPagination",
  props: {
    previous_page: String,
    next_page: String,
  },
  computed: {
    accessToken() {
      return Cookies("accessToken");
    },
  },
  methods: {
    push_data(url) {
      axios
        .get(url, {
          headers: { Authorization: `Bearer ${this.accessToken}` },
        })
        .then((response) => {
          this.$emit("change_orders", response.data); // This allows us to get the updated next and previous
        });
    },
  },
};
</script>
