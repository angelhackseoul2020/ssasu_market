<template>
  <div class="market">
      <Nav class="Nav"></Nav>
      <router-view />
  </div>
</template>

<script>
import Nav from "../components/market/Nav.vue";
export default {
    name: "Market",
    components: {
        Nav
    }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

.market {
    background: url('../assets/imgs/bgimg.png') center/cover no-repeat;
    height: 100vh;
    display: flex;
}

.Nav {
    width: 16%;
}
</style>