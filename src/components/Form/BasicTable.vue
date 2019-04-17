<template>
  <el-row style="margin-bottom: 30px">
    <el-col :span="24">
      <el-card>
        <el-row style="text-align: left;padding: 10px;font-size: 22px">
          <el-col :span="18">
            <span class="card-title">{{title}}</span>
          </el-col>
          <el-col :span="6">
            <el-button style="float: right" type="primary" @click="onClickAddNewRow">新增一行</el-button>
          </el-col>
        </el-row>
        <transition name="fade">
          <basic-table-new-row-form v-if="showNewRowForm" :table-name="tableName" :title="title+'-新增行'" :pdf-id="pdfId" :key-type-list="keyTypeList" :key-value-list="keyValueList" @sendCancelNewRowForm="showNewRowForm=false" @sendNewForm="onAddNewRow" :company-package-id="companyPackageId"></basic-table-new-row-form>
        </transition>
        <transition name="fade">
          <basic-table-edit-row-form v-if="showEditRowForm" :table-name="tableName" :pdfId="pdfId" :title="title+'-编辑行'" :key-type-list="keyTypeList" :key-value-list="keyValueList" :row-data="editRowData" @sendUpdateForm="onRowUpdate" :company-package-id="companyPackageId"></basic-table-edit-row-form>
        </transition>
        <el-table :data="tableData" border style="width: 100%;margin-top: 20px" v-if="startRender">
          <!--<el-table-column-->
          <!--prop="row_id"-->
          <!--label="row_id"-->
          <!--:v-show="false">-->
          <!--</el-table-column>-->
          <el-table-column
            v-for="(item,index) in Object.keys(keyValueList)"
            :prop="item"
            :label="keyValueList[item]"
            :show-overflow-tooltip=true>
            <template slot-scope="scope">
              <div v-if="keyTypeList[item]==='checkbox'">
                {{scope.row[item]=== false ? '否' : '是'}}
              </div>
              <div v-else>
                {{scope.row[item]}}
              </div>
            </template>
          </el-table-column>
          <el-table-column
            fixed="right"
            label="操作"
            width="90">
            <template slot-scope="scope">
              <el-button @click="onClickEditRow(scope.row)" type="text" size="small">编辑</el-button>
              <el-button @click="onClickDeleteRow(scope.row)" type="text" size="small">删除</el-button>

            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </el-col>

  </el-row>
</template>

<script>
  import { deleteTableRowData, getKeyValueList, getTableData } from '../../api/form'
  import BasicTableNewRowForm from './BasicTableNewRowForm'
  import BasicTableEditRowForm from './BasicTableEditRowForm'

  export default {
    name: 'BasicTable',
    components: { BasicTableEditRowForm, BasicTableNewRowForm },

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
        tableData: [],
        startRender: false,
        showNewRowForm: false,
        showEditRowForm: false,
        editRowData: {}
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
      getTableData(this.pdfId, this.tableName,this.companyPackageId).then(response => {
        let data = response.data
        if (data.code === 1) {
          this.tableData = data.tableData
          this.startRender = true
        } else {
          console.log('获取数据失败')
          console.log(response)
        }
      })
    },
    methods: {
      onClickEditRow(row) {
        this.editRowData = row
        this.showNewRowForm = false
        this.showEditRowForm = false
        this.$nextTick(() => {
          this.showEditRowForm = true

        })
      },
      onClickDeleteRow(row) {
        this.$confirm('此操作将永久删除该行, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          deleteTableRowData(row, this.tableName).then(response => {
            let res = response.data
            if (res.code === 1) {
              this.$message({
                message: '删除成功',
                type: 'success',
                duration: 1000,
                center: true
              })
              console.log(this.tableName + ' ' + this.field + ' ' + this.content, '自动保存成功')

            } else {
              this.$message.error({
                message: '删除失败',
                duration: 1000,
                center: true
              })
              console.log(this.tableName + ' ' + this.field + ' ' + this.content, '自动保存失败')
            }
          })
          this.tableData.splice(this.tableData.indexOf(row), 1)
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })

      },
      onClickAddNewRow() {
        this.showEditRowForm = false
        this.showNewRowForm = !this.showNewRowForm
      },
      onRowUpdate(form) {
        this.tableData.filter(function(item) {
            return item === form.row_id
          }
        )[0] = form
        console.log(form)
        this.showEditRowForm = false
      },
      onAddNewRow(form) {
        this.tableData.push(form)
        this.showNewRowForm = false
      }
    }
  }
</script>

<style scoped>
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }

  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
  {
    opacity: 0;
  }
</style>
