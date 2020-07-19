<template>
  <div id="summary">
    <span id="summary-name">{{name}}</span>
    <span id="to-detail">상세보기</span>
    <span id="summary-score">{{score}}</span>
    <span id="summary-star">{{star}}</span>
    <span id="summary-reviewcnt">리뷰 3건</span>
    <span id="summary-address">{{address}}</span>
    <span id="summary-working-time">영업시간 매일 09:00~18:00</span>
    <span id="summary-phone">02-8383-1221</span>
    <img src="../../assets/imgs/logo2.png" alt id="summary-market-img" />
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: Number
    },
    name: {
      type: String
    },
    score: {
      type: Number
    },
    star: {
      type: String
    },
    address: {
      type: String
    }
  },
  mounted() {
    var toDetail = document.getElementById("to-detail");
    toDetail.addEventListener("click", () => {
      this.$router.push("/home/" + this.id);
    });
  }
};
</script>

<style>
#summary {
  position: fixed;
  width: 800px;
  height: 350px;
  border-radius: 35px;
  top: 300px;
  left: 500px;
  background-color: white;
}
#summary-name {
  position: absolute;
  font-size: 35px;
  top: 25px;
  left: 25px;
}
#to-detail {
  position: absolute;
  font-size: 25px;
  top: 70px;
  left: 300px;
  color: red;
  cursor: pointer;
}
#summary-score {
  position: absolute;
  font-size: 30px;
  color: seagreen;
  top: 110px;
  left: 40px;
}
#summary-star {
  position: absolute;
  font-size: 40px;
  color: seagreen;
  top: 108px;
  left: 105px;
}
#summary-reviewcnt {
  position: absolute;
  font-size: 20px;
  top: 110px;
  left: 320px;
}
#summary-address {
  position: absolute;
  font-size: 25px;
  top: 150px;
  left: 35px;
}
#summary-working-time {
  position: absolute;
  font-size: 20px;
  top: 200px;
  left: 35px;
}
#summary-phone {
  position: absolute;
  font-size: 25px;
  top: 235px;
  left: 35px;
}
#summary-market-img {
  position: absolute;
  width: 300px;
  height: 250px;
  left: 450px;
  top: 50px;
}
</style>