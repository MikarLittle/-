<template>
  <el-table :data="tableData" stripe v-if="currValue === '2'"
  class='demos' height="400"
  :default-sort = "{prop: 'birthday', order: 'descending'}" ref="testTable">
    <el-table-column prop="child_name" label="孩子姓名" width="120">
    </el-table-column>
    <el-table-column prop="gender" label="孩子性别" width="60">
    </el-table-column>
    <el-table-column prop="parent_name" label="家长姓名" width="120">
    </el-table-column>
    <el-table-column prop="classin_id" label="classIn账号" width="120">
    </el-table-column>
    <el-table-column prop="classin_id" label="classIn账号" width="120">
    </el-table-column>
    <el-table-column prop="classin_name" label="classIn昵称" width="120">
    </el-table-column>
    <el-table-column prop="child_name" label="孩子姓名" width="120">
    </el-table-column>
    <el-table-column prop="birthday" label="生日" width="120">
    </el-table-column>
    <el-table-column prop="cc_name" label="顾问姓名" width="120">
    </el-table-column>
    <el-table-column prop="sign" label="是否报名" width="100">
    </el-table-column>
  </el-table>
</template>

<script>
/**
 * 显示孩子信息模块
 * @module childInformation
 */
import { getCookie } from '@/utils/utils';
import DIC from '@/dictionary.json';

export default {
  props: {
    initial: {
      default: '0',
    },
  },
  /**
   * @prop {String} currValue 判断当前页面状态
   * @prop {Boolean} isTrans 判断是否需要再次向后端发送请求
   * @prop {Array} tableData 存入孩子的具体信息
   */
  data() {
    return {
      currValue: '0',
      isTrans: true,
      tableData: [],
    };
  },
  watch: {
    initial(nv) {
      this.currValue = nv;
      if (nv === '2') {
        this.axios({
          method: 'post',
          url: 'customer/info',
          headers: { 'X-CSRFToken': getCookie('csrftoken') },
        }).then((response) => {
          if (response.data.msg === DIC.STATUS_CODE.Success && this.isTrans) {
            for (let i = 0; i < response.data.list.length; i += 1) {
              const info = {};
              info.child_name = response.data.list[i].child_name;
              info.gender = response.data.list[i].gender;
              info.parent_name = response.data.list[i].parent_name;
              info.classin_id = response.data.list[i].classin_id;
              info.classin_name = response.data.list[i].classin_name;
              info.birthday = response.data.list[i].birthday;
              info.cc_name = response.data.list[i].cc_name;
              info.audition_count = response.data.list[i].audition_count;
              if (response.data.list[i].is_signedup === true) {
                info.sign = '是';
              } else {
                info.sign = '否';
              }
              this.tableData.push(info);
            }
            this.isTrans = false;
          }
        });
      }
    },
  },
};
</script>

<style scoped>
.demos {
  margin: 0 auto;
  height: 55%;
  width: 85%;
  margin-top: 3.5%;
}
</style>
