<template>
  <div id="nav">
    <MessageBar></MessageBar>
    <NavBar></NavBar>
  </div>
  <router-view />
</template>

<script>
import NavBar from "./components/NavBar";
import MessageBar from "./components/MessageBar";

export default{

  components:{
      NavBar,
      MessageBar,
  }
}

</script>