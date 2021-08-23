<template>
  <div>
    <div class="container is-fluid">
      <HomeLatestItems></HomeLatestItems>
    </div>
    <HomeMission></HomeMission>
  </div>
</template>

<script>
// @ is an alias to /src
import HomeLatestItems from "../components/Home/HomeLatestItems";
import HomeMission from "../components/Home/HomeMission";

export default {
  name: "Home",
  components: {
    HomeLatestItems,
    HomeMission,
  },
};
</script>
