<template>
<div class="marketStoreWrap">
  <div class="marketStore">
    <div class="Header">
      <div class="marketName">광장시장</div>
      <div class="searchBar">
        <img class="searchIcon" src="../../assets/imgs/search.png" alt />
        <input type="text" placeholder="상점 및 품목 찾기" />
      </div>
    </div>
    <StoreCard></StoreCard>
    <StoreCard></StoreCard>
  </div>
</div>
</template>

<script>
import StoreCard from "./StoreCard.vue";
export default {
    name: "MarketStore",
    components: {
      StoreCard
    }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
    font-family: "Jua", sans-serif;
    box-sizing: border-box;
}
.marketStoreWrap {
    margin: 3rem 3rem;
}
.marketStore {
  width: 70%;
  margin: 0 auto;
}
.Header {
  width: 100%;
  margin: 0;
  display: flex;
}
.marketName {
  font-size: 3.5rem;
  color: #2E0202;
}
.searchBar {
  width: 300px;
  height: 50px;
  display: flex;
  position: absolute;
  right: 15%;
  background-color: #fdafd063;
  border-radius: 25px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
.searchIcon {
  width: 30px;
  margin: 10px;
}
input {
  outline: none;
  background-color: transparent;
  border: none;
  height: 50px;
  font-size: 30px;
  color: #3d0606b7;
  margin: 0;
}
input::placeholder {
  font-size: 2rem;
  color: #5a0909b7;
}
</style>