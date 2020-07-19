<template>
  <div>
    <div id="search-item" @click="open">
      <p id="search-market-name">{{marker.name}}</p>
      <p id="search-market-score">{{marker.avg_score}}</p>
      <p id="search-market-star">{{star}}</p>
      <p id="search-market-reviewcnt">{{marker.reviewcnt}}</p>
      <p id="search-market-address">{{marker.address}}</p>
      <p id="search-market-phone">{{marker.phone}}</p>
    </div>
    <Summary
      v-if="opensummary"
      :id="marker.id"
      :name="marker.name"
      :score="marker.avg_score"
      :star="star"
      :address="marker.address"
    />
  </div>
</template>

<script>
import Summary from "./Summary.vue";
export default {
  components: {
    Summary
  },
  props: {
    marker: {
      type: Object
    }
  },
  data() {
    return {
      star: "",
      opensummary: 0
    };
  },
  mounted() {
    if (this.marker.avg_score === 5) {
      this.star = "★★★★★";
    } else if (this.marker.avg_score >= 4.5) {
      this.star = "★★★★☆";
    } else if (this.marker.avg_score >= 4) {
      this.star = "★★★★";
    } else if (this.marker.avg_score >= 3.5) {
      this.star = "★★★☆";
    } else if (this.marker.avg_score >= 3) {
      this.star = "★★★";
    } else if (this.marker.avg_score >= 2.5) {
      this.star = "★★☆";
    } else if (this.marker.avg_score >= 2) {
      this.star = "★★";
    } else if (this.marker.avg_score >= 1.5) {
      this.star = "★☆";
    } else if (this.marker.avg_score >= 1) {
      this.star = "★";
    } else if (this.marker.avg_score >= 0.5) {
      this.star = "☆";
    } else {
      this.star = "";
    }
    console.log(this.marker);
  },
  methods: {
    open() {
      this.opensummary = 1;
    }
  }
};
</script>

<style>
#search-item {
  position: relative;
  width: 100%;
  padding: 20px 0;
  height: 180px;
  border-bottom: solid 1px black;
}
#search-market-name {
  position: absolute;
  font-size: 32px;
  margin: 0;
  left: 30px;
}
#search-market-score {
  position: absolute;
  top: 75px;
  font-size: 30px;
  margin: 0;
  left: 30px;
  color: darkcyan;
}
#search-market-star {
  position: absolute;
  top: 72px;
  font-size: 30px;
  margin: 0;
  left: 85px;
  color: darkcyan;
}
#search-market-address {
  position: absolute;
  top: 120px;
  font-size: 20px;
  margin: 0;
  left: 30px;
}
#search-market-phone {
  position: absolute;
  top: 150px;
  font-size: 20px;
  margin: 0;
  left: 30px;
  color: darkgreen;
}
#search-market-reviewcnt {
  position: absolute;
  top: 85px;
  font-size: 20px;
  margin: 0;
  left: 280px;
  color: grey;
}
</style>