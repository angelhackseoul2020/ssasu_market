<template>
  <div class="marketCommunityWrap">
    <div class="marketCommunity">
      <div class="Header">
        <div class="marketName">광장시장</div>
        <div class="searchBar">
          <img class="searchIcon" src="../../assets/imgs/search.png" alt />
          <input type="text" placeholder="검색" />
        </div>
        <router-link to="/market/write">
          <button class="write">
            <img class="writeIcon" src="../../assets/imgs/write.png" alt />
          </button>
        </router-link>
      </div>
      <!-- <router-link style="text-decoration: none; color: inherit;" to="/market/reviewdetail">
        <ReviewCard></ReviewCard>
      </router-link>-->
      <div id="ReviewList">
        <ReviewCard
          v-for="data in datas"
          :key="data"
          :title="data.title"
          :text="data.text"
          :score="data.score"
          :star="data.star"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ReviewCard from "./ReviewCard.vue";
export default {
  name: "MarketCommunity",
  data() {
    return {
      datas: [
        {
          title: "광장시장",
          text: "광장시장 좋아요",
          score: 5.0,
          star: "★★★★★"
        },
        {
          title: "광장시장1",
          text: "광장시장1 좋아요",
          score: 5.0,
          star: "★★★★★"
        },
        {
          title: "광장시장2",
          text: "광장시장2 좋아요",
          score: 5.0,
          star: "★★★★★"
        },
        {
          title: "광장시장3",
          text: "광장시장3 좋아요",
          score: 5.0,
          star: "★★★★★"
        }
      ]
    };
  },
  components: {
    ReviewCard
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
.marketCommunityWrap {
  margin: 3rem 3rem;
}
.marketCommunity {
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
  right: 25%;
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
.write {
  position: absolute;
  right: 15%;
  border-style: none;
  background-color: transparent;
  outline: 0;
}
.write:hover {
  cursor: pointer;
}
.writeIcon {
  width: 50px;
}
#ReviewList {
  position: absolute;
  overflow: auto;
  width: 55%;
  height: 80%;
}
#ReviewList::-webkit-scrollbar {
  width: 10px;
}
#ReviewList::-webkit-scrollbar-thumb {
  background-color: #88093e;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
}
#ReviewList::-webkit-scrollbar-track {
  background-color: rgba(221, 149, 149, 0.726);
  border-radius: 10px;
  box-shadow: inset 0px 0px 5px white;
}
</style>