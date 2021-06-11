<template>
  <el-row style="margin-bottom: 30px">
    <el-col :span="24">
      <el-card>
        <el-row style="text-align: left;padding: 10px;font-size: 22px">
          <span class="card-title">{{title}}</span>
        </el-row>
        <el-row>
          <el-row style="text-align: left;padding: 15px 10px 0px 10px;font-size: 14px">
            <span>标的公司组合名称</span>
          </el-row>
          <el-row style="padding: 10px">
            <el-input v-model="packageName"></el-input>
          </el-row>
        </el-row>
        <el-row>
          <el-row style="text-align: left;padding: 15px 10px 0px 10px;font-size: 14px">
            <span>请选择标的公司</span>
          </el-row>
          <el-row style="padding: 10px">
            <el-checkbox-group v-model="companyList">
              <div v-for="(item,index) in allCompany" style="padding: 5px">
                <el-checkbox :label="item.company.row_id" :disabled="item.used_flag" v-if="item.used_flag">{{item.company.target_company}}{{filterPackage(item.company.row_id)}}</el-checkbox>
                <el-checkbox :label="item.company.row_id" :disabled="item.used_flag" v-else>{{item.company.target_company}}</el-checkbox>
              </div>
            </el-checkbox-group>
          </el-row>
        </el-row>
        <el-row>
          <el-button type="primary" @click="onSubmit">立即生成表格</el-button>
        </el-row>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
  import { getAllCompany, saveCompanyPackage } from '../../api/form'

  export default {
    name: 'BasicNewTargetPackage',
    props: {
      'pdfId': '',
      'moduleName': '',
      'companyPackageList': {
        type: Array,
        default: []
      }
    },
    data() {
      return {
        title: '新增套件',
        companyList: [],
        packageName: '',
        allCompany: []
      }
    },

    methods: {
      onSubmit() {
        if (this.packageName === '') {
          this.$message({
            message: '请先填写标的公司组合名称',
            type: 'error'
          })
        } else if (this.companyList.length === 0) {
          this.$message({
            message: '请至少选择一个标的公司',
            type: 'error'
          })
        } else {
          saveCompanyPackage(this.pdfId, this.moduleName, this.packageName, this.companyList).then(response => {
            let res = response.data
            if (res.code === 1) {
              this.$emit('sendNewTargetPackage')
            } else {
              this.$message({
                message: '保存出错',
                type: 'error'
              })
            }
          }).catch(exception => {
            console.log(exception)
          })
        }
      },
      filterPackage(company_id) {
        let companyPackageList = this.companyPackageList
        for (let item of companyPackageList) {
          if (item.company_id_list.find(value => parseInt(value) === company_id)) {
            return '——包含在组合：' + item.package_name
          }
        }
        return ''
      }

    },
    mounted() {
      getAllCompany(this.pdfId, this.moduleName).then(response => {
        let res = response.data
        if (res.code === 1) {
          this.allCompany = res.data
        }
      }).catch(except => {
        console.log(except)
      })
    }
  }
</script>

<style scoped>

</style>
