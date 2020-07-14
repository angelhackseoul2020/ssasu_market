<template>
  <div class="marketInfoWrap">
    <div class="marketInfo">
      <div class="marketName">
        광장시장
      </div>

      <div class="starReview">
        <!-- starComponent -->
        <div>5.0 ★★★★★</div>
        <div class="reviewNum">리뷰 3건</div>
      </div>

      <div class="aboutMarket">
        <div class="textInfo">
          <div class="address">
            서울 종로구 창경궁로 88
          </div>
          <div class="time">
            영업시간 매일 09:00 ~ 18:00
          </div>
          <div class="tell">
            02-2267-0291
          </div>
          <div class="utility">
            시설정보
            <div class="utilIcon">
              <img class="park" src="../../assets/imgs/park.png" alt="">
              <img class="toilet" src="../../assets/imgs/toilet.png" alt="">
            </div>
          </div>
        </div>
        <div class="photoInfo">
          사진
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
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
  color: #2E0202;
}
.starReview {
  display: flex;
  justify-content: center;
  font-size: 1.5rem;
  color: #2E0202;
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
  color: #2A7E05; 
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