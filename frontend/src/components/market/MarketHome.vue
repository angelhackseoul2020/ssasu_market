<template>
  <div class="home">
      <MarketInfo></MarketInfo>
      <MarketVisit></MarketVisit>
  </div>
</template>

<script>
import MarketInfo from "./MarketInfo.vue";
import MarketVisit from "./MarketVisit.vue";

export default {
    name: "MarketHome",
    components: {
        MarketInfo,
        MarketVisit
    }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
    font-family: "Jua", sans-serif;
    margin: 3rem 3rem;
}
</style>