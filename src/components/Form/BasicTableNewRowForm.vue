<template>
  <el-row>
    <el-col :span="spanWidth">
      <el-card>
        <el-row style="text-align: left;padding: 10px;font-size: 22px">
          <span class="card-title">{{title}}</span>
        </el-row>
        <el-row v-for="(item,index) in Object.keys(keyValueList)" :key="index" v-if="startRender">
          <el-row style="text-align: left;padding: 15px 10px 0px 10px;font-size: 14px">
            <span v-if="keyTypeList[item]!=='checkbox'">{{keyValueList[item]}}</span>
          </el-row>
          <el-row>
            <edit-input v-if="keyTypeList[item]==='text'||keyTypeList[item]==='textarea'" :type="keyTypeList[item]" :pdfId="pdfId" :name="item" :table-name="tableName" :field="item" edit-content="" :auto-save="false" :auto-callback="true" @sendInputChange="onInputChange"/>
            <edit-number v-else-if="keyTypeList[item]==='ratio'||keyTypeList[item]==='decimal'||keyTypeList[item]==='int'" :type="keyTypeList[item]" :pdfId="pdfId" :name="item" :table-name="tableName" :field="item" :edit-content="form[item]" :auto-save="false" :auto-callback="true"
                         @sendInputChange="onInputChange"/>
            <edit-checkbox v-else-if="keyTypeList[item]==='checkbox'" :label="keyValueList[item]" :pdfId="pdfId" :name="item" :table-name="tableName" :field="item" edit-content="" :auto-save="false" :auto-callback="true" @sendInputChange="onInputChange"/>
            <edit-date-picker v-else-if="keyTypeList[item]==='datetime'" :pdfId="pdfId" :table-name="tableName" :field="item" :edit-content="form[item]" :auto-save="false" :auto-callback="true" @sendInputChange="onInputChange"/>
          </el-row>
        </el-row>
        <div style="margin-top: 10px;padding: 10px">
          <el-button type="primary" @click="onSaveTableRowData">保存</el-button>
          <!--<el-button type="primary" @click="onReset">重置</el-button>-->
          <el-button @click="onCancel">取消</el-button>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
  import EditInput from '../Common/EditInput'
  import { getKeyValueList, saveTableRowData } from '../../api/form'
  import EditCheckbox from '../Common/EditCheckbox'
  import EditDatePicker from '../Common/EditDatePicker'
  import EditNumber from '../Common/EditNumber'

  export default {
    name: 'BasicTableNewRowForm',
    props: {
      'title': '',
      'tableName': '',
      'pdfId': '',
      'companyPackageId': {
        default: -1
      },
      spanWidth: {
        default: 24
      },
      keyValueList: {},
      keyTypeList: {}
    },
    data() {
      return {
        startRender: false,
        form: {}

      }
    },
    mounted() {
      let keyTypeList = this.keyTypeList
      let obj = {}
      for (let fieldName of Object.keys(keyTypeList)) {
        if (keyTypeList[fieldName] === 'checkbox') {
          obj[fieldName] = false
        } else {
          obj[fieldName] = null
        }
      }
      obj['pdf_id'] = this.pdfId
      obj['company_package_id'] = this.companyPackageId
      console.log(obj)
      this.form = obj
      this.startRender = true
      // getNewRowData(this.pdfId, this.tableName).then(response => {
      //   let data = response.data
      //   if (data.code === 1) {
      //     this.form = data.formData
      //     this.startRender = true
      //   } else {
      //     console.log('获取数据失败')
      //     console.log(response)
      //   }
      // })
    },
    methods: {
      onReset() {

      },
      onInputChange(field, content) {
        this.form[field] = content
      },
      onSaveTableRowData() {
        console.log(this.form)
        saveTableRowData(this.form, this.tableName).then(response => {
          let res = response.data
          if (res.code === 1) {
            this.$message({
              message: '保存成功',
              type: 'success',
              duration: 1000,
              center: true
            })
            this.form = res.data
            this.$emit('sendNewForm', this.form)
          } else {
            this.$message.error({
              message: '保存失败',
              duration: 1000,
              center: true
            })
          }
        })

      },

      onCancel() {
        this.$emit('sendCancelNewRowForm')
      }
    },
    components: { EditNumber, EditDatePicker, EditCheckbox, EditInput }
  }
</script>

<style scoped>

</style>

