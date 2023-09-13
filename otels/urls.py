from django.urls import path

from otels.views import *

urlpatterns = [
    # path('minisearch', OtelMiniList.as_view(), name='otel-mini-search'),
    path('minisearch', MiniSearchApiView.as_view(), name='otel-mini-search'),
    path('otels', OtelList.as_view(), name='Otel list'),
    path('otel/<int:id>', OtelChange.as_view(), name='Otel Change'),
    path('otelchains', OtelChainList.as_view(), name='Otel Chain list'),
    path('otelchain/<int:id>', OtelChainChange.as_view(), name='Otel Chain Change'),
    path('otelcategories', OtelCategoryList.as_view(), name='Otel Category lists'),
    path('otelcategory/<int:id>', OtelCategoryChange.as_view(),
         name='Otel Category Change'),
    path('airports', AirportList.as_view(), name='AirPorts list'),
    path('airport/<int:id>', AirportChange.as_view(), name='AirPort Change'),
    path('contracts', ContractList.as_view(), name='Contract lists'),
    path('contract/<int:id>', ContractChange.as_view(), name='Contract Change'),
    path('files', UploadFileList.as_view(), name='UploadFile-lists'),
    path('file/<int:id>', UploadFileChange.as_view(),
         name='UploadFile-Change'),
    path('otelservicecategories', OtelServiceCategoryList.as_view(),
         name='Otel Service Category lists'),
    path('otelservicecatgory/<int:id>', OtelServiceCategoryChange.as_view(),
         name='Otel Service Category Change'),
    path('oteltypes', OtelTypeList.as_view(),
         name='Otel Service Category lists'),
    path('oteltype/<int:id>', OtelTypeChange.as_view(),
         name='Otel Service Category Change'),
    path('otelservicedetails', OtelFacilityDetailList.as_view()),
    path('otelservicedetail/<int:id>', OtelFacilityDetailChange.as_view(),
         name='Otel Facility Detail Change'),
    path('otelfeatures', OtelFeaturesList.as_view(), name='Otel Feature  lists'),
    path('otelfeature/<int:id>', OtelFeaturesChange.as_view(),
         name='Otel Features Change'),
    path('otelimages', OtelImagesList.as_view(), name='Otel Image lists'),
    path('otelimage/<int:id>', OtelImagesChange.as_view(),
         name='Otel Image Change'),
    path('customerpaymenttypes', CustomerPaymentTypeList.as_view(),
         name='Customer Payment Type List'),
    path('customerpaymenttype/<int:id>', CustomerPaymentTypeChange.as_view(),
         name='Customer Payment Type Change'),
    path('otelcontractpaymenttypes', OtelContractPaymentTypeList.as_view(),
         name='Otel Contract Payment Type lists'),
    path('otelcontractpaymenttype/<int:id>', OtelContractPaymentTypeChange.as_view(),
         name='Otel Contract Payment Type Change'),
    path('otelthemes', OtelThemeList.as_view(), name='Otel Tema lists'),
    path('oteltheme/<int:id>', OtelThemeChange.as_view(), name='Otel Tema Change'),
    path('otelservicedescriptions', OtelServiceDescriptionList.as_view(),
         name='Otel hizmetleri açıklama lists'),
    path('otelservicedescription/<int:id>', OtelServiceDescriptionChange.as_view(),
         name='Otel hizmetleri açıklama Change'),
    path('periodicdescriptions', PeriodicDescriptionList.as_view(),
         name='Dönemsel açıklama lists'),
    path('periodicdescription/<int:id>',
         PeriodicDescriptionChange.as_view(), name='Dönemsel açıklama Change'),
    path('periodicdescriptiontypes', PeriodicDescriptionTypeList.as_view(),
         name='Dönemsel açıklama tipi lists'),
    path('periodicdescriptiontype/<int:id>',
         PeriodicDescriptionTypeChange.as_view(), name='Dönemsel açıklama tipi Change'),
    path('stakeholders', StakeHolderContactList.as_view(),
         name='Otel yetkilisi lists'),
    path('stakeholder/<int:id>', StakeHolderContactChange.as_view(),
         name='Otel yetkilisi Change'),
    path('suppliers', SupplierList.as_view(), name='Supplier List'),
    path('supplier/<int:id>', SupplierChange.as_view(), name='Supplier Change'),
    path('payatfaroomcilities', PayAtFacilityList.as_view(),
         name='PayAtFacility List'),
    path('payatfacility/<int:id>', PayAtFacilityChange.as_view(),
         name='PayAtFacility Change'),
    path('payatfacilities', PayAtFacilityList.as_view(), name='PayAtFacility List'),
    path('paymentplans', PaymentPlanList.as_view(), name='Payment plan List'),
    path('paymentplan/<int:id>', PaymentPlanChange.as_view(),
         name='Payment Plan Change'),
    path('pensiontypeperiodicdescriptions', PensionTypePeriodicDescriptionList.as_view(
    ), name='Odatipi dönemsel açıklama lists'),
    path('pensiontypeperiodicdescription/<int:id>',
         PensionTypePeriodicDescriptionChange.as_view(), name='Odatipi dönemsel açıklama Change'),
    path('banks', BankList.as_view(), name='Bank List'),
    path('bank/<int:id>', BankChange.as_view(), name='Bank Change'),
    path('otelowners', OtelOwnerList.as_view(), name='otel-owner-list'),
    path('otelowner/<int:id>', OtelOwnerChange.as_view(), name='otel-owner-change'),
    path('bankaccountinfos', AccountInfoList.as_view(), name='AccountInfo List'),
    path('bankaccountinfo/<int:id>',
         AccountInfoChange.as_view(), name='AccountInfo Change'),

    path('ccinterestratios', CCInterestRatioList.as_view(),
         name='CCInterestRatioList'),
    path('ccinterestratio/<int:id>', CCInterestRatioChange.as_view(),
         name='CCInterestRatio Change'),

    path('modulepaymentinfos', ModulPaymentAccountInfoList.as_view(),
         name='ModulPaymentAccountInfo List'),
    path('modulepaymentinfo/<int:id>', ModulPaymentAccountInfoChange.as_view(),
         name='ModulPaymentAccountInfo Change'),

    path('otelgroups', HotelGroupList.as_view(), name='HotelGroup List'),
    path('otelgroup/<int:id>', HotelGroupChange.as_view(),
         name='HotelGroup Change'),

    path('epidemicmeasures', EpidemicMeasuresList.as_view(),
         name='EpidemicMeasures List'),
    path('epidemicmeasure/<int:id>', EpidemicMeasuresChange.as_view(),
         name='EpidemicMeasures Change'),


    path('contractitems', ContractItemsApprovalList.as_view(),
         name='ContractItemsApproval List'),
    path('contractitem/<int:id>', ContractItemsApprovalChange.as_view(),
         name='ContractItemsApproval Change'),

    path('invoiceinfos', InvoiceInfoList.as_view(), name='InvoiceInfo List'),
    path('invoiceinfo/<int:id>', InvoiceInfoChange.as_view(),
         name='InvoiceInfo Change'),

    path('chilconditionthemes', ChilConditionThemeList.as_view(),
         name='ChilCondition Theme List'),
    path('chilconditiontheme/<int:id>', ChilConditionThemeChange.as_view(),
         name='ChilCondition Theme Change'),

    path('searchlogs', SearchLogList.as_view(), name='SearchLog List'),
    path('searchlog/<int:id>', SearchLogChange.as_view(), name='SearchLog Change'),
    path('search', SearchApiView.as_view(), name='search'),
    # path('embeddedsearch', EmbeddedSearchView.as_view(), name='embeddedsearch'),
    path('uploadimages', UploadImage.as_view(), name='uploadimages'),
    # path('search2', cache_page(60 * 15) (SearchApiView.as_view()), name = 'search'),
    path('reservationsearch', ReservationSearch.as_view(), name='searchquota'),
    path('checkpricestatus', CheckPriceStatus.as_view(), name='checkpricestatus'),
    path('pricecostinfo', PriceCostInfo.as_view(), name='pricecostinfo'),

    path('brokenprices', BrokenPriceList.as_view(),
         name='brokenprice-list'),
    path('brokenprice/<int:id>', BrokenPriceChange.as_view(),
         name='brokenprice-change'),

]
