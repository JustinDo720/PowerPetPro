<template>
  <div id="nav">
    <MessageBar></MessageBar>
    <NavBar></NavBar>
    <router-view />
    <Footer></Footer>
  </div>

</template>

<script>
import NavBar from "./components/NavBar";
import MessageBar from "./components/MessageBar";
import Footer from "./components/Footer";

export default{

  components:{
      NavBar,
      MessageBar,
      Footer
  }
}

</script>