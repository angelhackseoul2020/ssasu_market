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
      <div id="StoreList">
        <StoreCard
          v-for="data in datas"
          :key="data"
          :name="data.name"
          :address="data.address"
          :tell="data.tell"
        />
      </div>
    </div>
  </div>
</template>

<script>
import StoreCard from "./StoreCard.vue";
export default {
  name: "MarketStore",
  data() {
    return {
      datas: [
        {
          name: "신라한복",
          address: "서울특별시 종로구 예지도 6-1 광장시장 1층 134-1호",
          tell: "02-2275-9003"
        },
        {
          name: "신라한복2",
          address: "서울특별시 종로구",
          tell: "02-2275"
        },
        {
          name: "신라한복3",
          address: "서울특별시 종로구3",
          tell: "02-2275"
        },
        {
          name: "신라한복4",
          address: "서울특별시 종로구4",
          tell: "02-2275"
        },
        {
          name: "신라한복5",
          address: "서울특별시 종로구5",
          tell: "02-2275"
        }
      ]
    };
  },
  components: {
    StoreCard
  }
};
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
  color: #2e0202;
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
#StoreList {
  position: absolute;
  overflow: auto;
  width: 55%;
  height: 80%;
}
#StoreList::-webkit-scrollbar {
  width: 10px;
}
#StoreList::-webkit-scrollbar-thumb {
  background-color: #88093e;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
}
#StoreList::-webkit-scrollbar-track {
  background-color: rgba(221, 149, 149, 0.726);
  border-radius: 10px;
  box-shadow: inset 0px 0px 5px white;
}
</style>