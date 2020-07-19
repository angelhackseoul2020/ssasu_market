<template>
  <div class="market">
    <Nav class="Nav" :home="homeNum"></Nav>
    <router-view class="marketRouter" @marketNum="marketNum" />
  </div>
</template>

<script>
import Nav from "../components/market/Nav.vue";
export default {
  data() {
    return {
      homeNum: 0
    };
  },
  methods: {
    marketNum(event) {
      this.homeNum = event * 1;
    }
  },
  name: "Market",
  components: {
    Nav
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");

.market {
  background: url("../assets/imgs/bgimg.png") center/cover no-repeat;
  height: 100vh;
  display: flex;
}

.Nav {
  width: 16%;
}

.marketRouter {
  width: 84%;
}
</style>