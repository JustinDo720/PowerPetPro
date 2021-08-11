<template>
  <div id="nav">
    <NavBar></NavBar>
  </div>
  <router-view />
</template>

<script>
import NavBar from "./components/NavBar";

export default{

  components:{
      NavBar
  }
}

</script>