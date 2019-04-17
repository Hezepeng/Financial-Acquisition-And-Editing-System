import axios from 'axios'
import qs from 'qs'

const request = axios.create({
  baseURL: 'http://localhost:8000', // api的base_url
  timeout: 5000 // 请求超时时间
})

export function fileDownload(json_data) {
  return request({
    url: '/manager/downloadTimeLine',
    method: 'post',
    headers: { 'Content-Type': 'multipart/form-data' },
    data: json_data,
    responseType: 'arraybuffer'

  })
}

export function getKeyValueList(tableName) {
  return request({
    url: '/api/getKeyValueList',
    method: 'get',
    params: {
      tableName
    }
  })
}

export function getTableRowData(pdfId, tableName, rowId) {
  return request({
    url: '/api/getTableRowData',
    method: 'get',
    params: {
      pdfId,
      tableName,
      rowId
    }
  })
}

export function getTableData(pdfId, tableName, companyPackageId) {
  return request({
    url: '/api/getTableData',
    method: 'get',
    params: {
      pdfId,
      tableName,
      companyPackageId
    }
  })
}

export function getFormData(pdfId, tableName, companyPackageId) {
  return request({
    url: '/api/getFormData',
    method: 'get',
    params: {
      pdfId,
      tableName,
      companyPackageId
    }
  })
}

export function saveSingleData(pdfId, tableName, rowId, field, editContent, companyPackageId) {
  let data = { 'pdfId': pdfId, 'tableName': tableName, 'rowId': rowId, 'field': field, 'editContent': editContent, 'companyPackageId': companyPackageId }
  return request({
    url: '/api/saveSingleData',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: qs.stringify(data)
  })
}

export function saveTableRowData(rowData, tableName) {
  let data = { 'rowData': rowData, 'tableName': tableName }
  return request({
    url: '/api/saveTableRowData',
    method: 'post',
    headers: { 'Content-Type': 'application/json' },
    data: data
  })
}

export function deleteTableRowData(rowData, tableName) {
  let data = { 'rowData': rowData, 'tableName': tableName }
  return request({
    url: '/api/deleteTableRowData',
    method: 'post',
    headers: { 'Content-Type': 'application/json' },
    data: data
  })
}

export function getPdf(pdfId, tableName) {
  return request({
    url: '/api/getPdf',
    method: 'get',
    params: {
      pdfId,
      tableName
    }
  })
}

export function deletePdf(pdfId) {
  return request({
    url: '/api/deletePdf',
    method: 'get',
    params: {
      pdfId,
    }
  })
}

export function getAllCompany(pdfId, moduleName) {
  return request({
    url: '/api/getAllCompany',
    method: 'get',
    params: {
      pdfId,
      moduleName
    }
  })
}

export function getAllCompanyPackage(pdfId, moduleName) {
  return request({
    url: '/api/getAllCompanyPackage',
    method: 'get',
    params: {
      pdfId,
      moduleName
    }
  })
}

export function saveCompanyPackage(pdfId, moduleName, packageName, companyList) {
  let data = { 'pdfId': pdfId, 'moduleName': moduleName, 'packageName': packageName, 'companyList': companyList }
  return request({
    url: '/api/saveCompanyPackage',
    method: 'post',
    headers: { 'Content-Type': 'application/json' },
    data: data
  })
}

export function deleteCompanyPackage(rowId) {
  let data = { 'rowId': rowId }
  return request({
    url: '/api/deleteCompanyPackage',
    method: 'post',
    headers: { 'Content-Type': 'application/json' },
    data: data
  })
}
