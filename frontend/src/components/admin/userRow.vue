<template>
  <div id="rowForm" @click="openAddModal">
    <p id='rowUserId'>{{uid}}</p>
    <p id='rowUserNick'>{{nick}}</p>
    <p id='rowUserAddress'>{{address}}</p>
    <p id='rowReviewCnt'>{{reviewcnt}}</p>
  </div>
</template>

<script>
export default {
  props:{
    index:{
      type:Number
    },
    uid:{
      type:String
    },
    nick:{
      type:String
    },
    address:{
      type:String
    },
    reviewcnt:{
      type:String
    }
  },
  data(){
    return{
    }
  },
  mounted(){
  },
  methods:{
    openAddModal(){
      this.$emit('openAddModal',this.index)
    }
  }
}
</script>

<style>
#rowForm{
  position: relative;
  width: 80%;
  font-size: 30px;
  height: 50px;
  padding: 5px 0 5px 0;
  margin-left: 10%;
  margin-right: 10%;
  border-bottom: solid 1px #bbbbbb;
}
#rowUserId{
  position: absolute;
  height: 30px;
  width:15%;
  text-align: center;
}
#rowUserNick{
  position: absolute;
  height: 30px;
  left: 15%;
  width: 25%;
  text-align: center;
}
#rowUserAddress{
  position: absolute;
  height: 30px;
  left: 40%;
  width: 35%;
  text-align: center;
}
#rowReviewCnt{
  position: absolute;
  height: 30px;
  left: 75%;
  width: 25%;
  text-align: center;
}
</style>