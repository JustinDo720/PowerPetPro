<template>
  <div class="container is-max-widescreen">
    <HomeLatestItems></HomeLatestItems>
  </div>
</template>

<script>
// @ is an alias to /src
import HomeLatestItems from "../components/Home/HomeLatestItems";

export default {
  name: "Home",
  components: {
    HomeLatestItems
  },
};
</script>
