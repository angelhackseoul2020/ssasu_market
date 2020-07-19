<template>
  <div id="rowForm" @click="openAddStore">
    <p id='rowId'>{{id}}</p>
    <p id='rowName'>{{name}}</p>
    <p id='rowSort'>{{sort}}</p>
    <p id='rowAddress'>{{address}}</p>
    <p id='rowMarket'>{{market}}</p>
  </div>
</template>

<script>
export default {
  props:{
    index:{
      type:Number
    },
    id:{
      type:String
    },
    name:{
      type:String
    },
    sort:{
      type:String
    },
    address:{
      type:String
    },
    market:{
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
    openAddStore(){
      console.log(this.index);
      this.$emit('openModalStore',this.index)
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
#rowId{
  position: absolute;
  height: 30px;
  width:10%;
  text-align: center;
}
#rowName{
  position: absolute;
  height: 30px;
  left: 10%;
  width: 20%;
  text-align: center;
}
#rowSort{
  position: absolute;
  height: 30px;
  left: 30%;
  width: 15%;
  text-align: center;
}
#rowAddress{
  position: absolute;
  height: 30px;
  left: 45%;
  width: 35%;
  text-align: center;
}
#rowMarket{
  position: absolute;
  height: 30px;
  left: 80%;
  width: 20%;
  text-align: center;
}


</style>