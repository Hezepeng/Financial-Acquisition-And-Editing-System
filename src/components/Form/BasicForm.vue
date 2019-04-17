<template>
  <el-row style="margin-bottom: 30px">
    <el-col :span="24">
      <el-card>
        <el-row style="text-align: left;padding: 10px;font-size: 22px">
          <span class="card-title">{{title}}</span>
        </el-row>
        <el-row v-for="(item,index) in Object.keys(keyValueList)" :key="index" v-if="startRender">
          <el-row style="text-align: left;padding: 15px 10px 0px 10px;font-size: 14px">
            <span v-if="keyTypeList[item]!=='checkbox'">{{keyValueList[item]}}</span>
          </el-row>
          <el-row>
            <edit-input v-if="keyTypeList[item]==='text'||keyTypeList[item]==='textarea'" :type="keyTypeList[item]" :pdfId="pdfId" :name="item" :table-name="tableName" :field="item" :edit-content="form[item]" :company-package-id="companyPackageId" :row-id="rowId"/>
            <edit-number v-else-if="keyTypeList[item]==='ratio'||keyTypeList[item]==='decimal'||keyTypeList[item]==='int'" :type="keyTypeList[item]" :pdfId="pdfId" :name="item" :table-name="tableName" :field="item" :edit-content="form[item]" :company-package-id="companyPackageId" :row-id="rowId"/>
            <edit-checkbox v-else-if="keyTypeList[item]==='checkbox'" :label="keyValueList[item]" :pdfId="pdfId" :name="item" :table-name="tableName" :field="item" :edit-content="form[item]" :company-package-id="companyPackageId" :row-id="rowId"/>
            <edit-date-picker v-else-if="keyTypeList[item]==='datetime'" :pdfId="pdfId" :table-name="tableName" :field="item" :edit-content="form[item]" :company-package-id="companyPackageId" :row-id="rowId"/>
          </el-row>
        </el-row>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
  import EditInput from '../Common/EditInput'
  import { getKeyValueList, getFormData } from '../../api/form'
  import EditCheckbox from '../Common/EditCheckbox'
  import EditDatePicker from '../Common/EditDatePicker'
  import EditNumber from '../Common/EditNumber'

  export default {
    name: 'BasicForm',
    props: {
      'title': '',
      'tableName': '',
      'pdfId': '',
      'companyPackageId': {
        default: -1
      }
    },
    data() {
      return {
        keyValueList: {},
        keyTypeList: {},
        form: {},
        startRender: false,
        rowId: null
      }
    },
    mounted() {
      getKeyValueList(this.tableName).then(response => {
        let data = response.data
        if (data.code === 1) {
          this.keyTypeList = data.keyTypeList
          this.keyValueList = data.keyValueList
        } else {
          console.log('获取数据失败')
          console.log(response)
        }
      })
      getFormData(this.pdfId, this.tableName, this.companyPackageId).then(response => {
        let data = response.data
        if (data.code === 1) {
          this.form = data.formData
          this.startRender = true
          this.rowId = data.formData.row_id
        } else {
          console.log('获取数据失败')
          console.log(response)
        }
      })
    },
    components: { EditNumber, EditDatePicker, EditCheckbox, EditInput }
  }
</script>

<style scoped>

</style>

