<template>
  <div class="marketInfoWrap">
    <div class="marketInfo">
      <div class="marketName">{{name}}</div>

      <div class="starReview">
        <!-- starComponent -->
        <div>{{score}} {{star}}</div>
        <div class="reviewNum">리뷰 {{reviewNum}}건</div>
      </div>

      <div class="aboutMarket">
        <div class="textInfo">
          <div class="address">{{address}}</div>
          <div class="time">{{time}}</div>
          <div class="tell">{{tell}}</div>
          <div class="utility">
            시설정보
            <div class="utilIcon">
              <img class="park" src="../../assets/imgs/park.png" alt />
              <img class="toilet" src="../../assets/imgs/toilet.png" alt />
            </div>
          </div>
        </div>
        <div class="photoInfo">사진</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MarketInfo",
  props: {
    name: {
      type: String
    },
    score: {
      type: Number
    },
    star: {
      type: String
    },
    reviewNum: {
      type: Number
    },
    address: {
      type: String
    },
    time: {
      type: String
    },
    tell: {
      type: String
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
.marketInfo {
  width: 70%;
  margin: 0 auto;
}
.marketName {
  text-align: center;
  font-size: 3.5rem;
  color: #2e0202;
}
.starReview {
  display: flex;
  justify-content: center;
  font-size: 1.5rem;
  color: #2e0202;
}
.reviewNum {
  padding-left: 20px;
}
.aboutMarket {
  display: flex;
  justify-content: center;
}
.textInfo {
  width: 60%;
  padding-top: 2%;
}
.address {
  font-size: 1.8rem;
}
.time {
  font-size: 1.3rem;
}
.tell {
  font-size: 1.2rem;
  color: #2a7e05;
}
.utility {
  padding-top: 20px;
  padding-bottom: 20px;
  font-size: 1.3rem;
}
.utilIcon img {
  width: 50px;
  margin-right: 10px;
}
.photoInfo {
  padding-top: 2%;
  padding-left: 3%;
  width: 40%;
}
</style>