"""
URL configuration for Easy_learn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home),

    path('login/', views.login),
    path('login_post/', views.login_post),

    path('cng_pswrd/', views.cng_pswrd),
    path('cng_pswrd_pst/', views.cng_pswrd_pst),
    path('admin_add_ration_product_post/', views.admin_add_ration_product_post),
    path('admin_add_ration_product/', views.admin_add_ration_product),
    path('admin_add_ration_product_post/', views.admin_add_ration_product_post),
    path('admin_view_rationproduct/', views.admin_view_rationproduct),
    path('admin_delete_product/<id>/', views.admin_delete_product),
    path('admin_edit_product/<id>/', views.admin_edit_product),
    path('admin_edit_product_post/', views.admin_edit_product_post),


    path('admin_add_ration_card/', views.admin_add_ration_card),
    path('admin_add_ration_card_post/', views.admin_add_ration_card_post),
    path('admin_view_rationcardtype/', views.admin_view_rationcardtype),
    path('admin_delete_ration_cardtype/<id>', views.admin_delete_ration_cardtype),
    path('admin_edit_ration_cardtype/<id>', views.admin_edit_ration_cardtype),
    path('admin_edit_rationcardtype_post/', views.admin_edit_rationcardtype_post),

    path('admin_add_statecenters/', views.admin_add_statecenters),
    path('admin_add_statecenters_post/', views.admin_add_statecenters_post),
    path('admin_view_statecenters/', views.admin_view_statecenters),
    path('admin_delete_statecenters/<id>', views.admin_delete_statecenters),
    path('admin_edit_statcenteres/<id>', views.admin_edit_statcenteres),
    path('admin_edit_statecenters_post/', views.admin_edit_statecenters_post),





    #user
    path('register/', views.register),
    path('register_pst/', views.register_pst),

    path('u_cng_pswrd/', views.u_cng_pswrd),
    path('u_cng_pswrd_pst/', views.u_cng_pswrd_pst),

    path('user_home/', views.user_home),

    # path('view_profile/', views.view_profile),

    # path('edit_prof/', views.edit_prof),
    # path('edit_prof_pst/', views.edit_prof_pst),

    path('user_send_complaint/', views.user_send_complaint),
    path('user_send_complaint_post/', views.user_send_complaint_post),

    path('view_reply/', views.view_reply),
    path('view_reply_post/', views.view_reply_post),


    path('logout/', views.logout),
    path('alogout/', views.logout),


    ############center

    path('statecenter_home/',views.statecenter_home),
    path('stategovernement_adddistrict/',views.stategovernement_adddistrict),
    path('stategovernement_adddistrict_post/',views.stategovernement_adddistrict_post),
    path('state_view_district/',views.state_view_district),
    path('stategovernement_addarea/',views.stategovernement_addarea),
    path('stategovernemnet_area_post/',views.stategovernemnet_area_post),
    path('state_delete_district/<id>',views.state_delete_district),
    path('state_view_area/',views.state_view_area),
    path('state_delete_area/<id>',views.state_delete_area),
    path('state_delete_scheme/<id>',views.state_delete_scheme),
    path('state_addsupplyco/',views.state_addsupplyco),
    path('state_addsuplycopost/',views.state_addsuplycopost),
    path('view_supplyco/',views.view_supplyco),
    path('state_add_rationcard/',views.state_add_rationcard),
    path('state_add_rationcard_post/',views.state_add_rationcard_post),
    path('view_card/',views.view_card),
    path('searchcard/',views.searchcard),
    path('delete_supplyco/<id>',views.delete_supplyco),


    ####supplyco


    path('supplyco_view_card/',views.supplyco_view_card),
    path('supplyco_searchcard/',views.supplyco_searchcard),
    path('supplyco_home/',views.supplyco_home),
    path('supplyco_view_notification/',views.supplyco_view_notification),
    path('supplyco_view_notification_search/',views.supplyco_view_notification_search),




    #farmer
path('user_signup/',views.user_signup),
path('user_signup_post/',views.user_signup_post),
path('user_viewprofile/',views.user_viewprofile),
path('farmer_home/',views.farmer_home),
path('stategovt_send_notice_to_collect_crops/',views.stategovt_send_notice_to_collect_crops),
path('stategovt_send_notice_to_collect_crops_post/',views.stategovt_send_notice_to_collect_crops_post),
path('state_view_notification/',views.state_view_notification),
path('state_view_notification_search/',views.state_view_notification_search),
path('state_delete_notification/<id>',views.state_delete_notification),
path('farmer_view_notification/',views.farmer_view_notification),
path('farmer_add_items/<nid>/<pid>',views.farmer_add_items),
path('farmer_add_item_post/',views.farmer_add_item_post),
path('add_family_member_post/',views.add_family_member_post),
path('add_family_member/<id>',views.add_family_member),
path('view_family_member/<id>',views.view_family_member),
path('supplyco_add_transactions/<rationid>',views.supplyco_add_transactions),
path('supplyco_add_trans_post/',views.supplyco_add_trans_post),
path('supplyco_add_trans_post/',views.supplyco_add_trans_post),
path('supplyco_view_notification_response/<id>',views.supplyco_view_notification_response),
path('statecenter_view_notification_response/<id>',views.statecenter_view_notification_response),
path('user_view_itemss/',views.user_view_itemss),
path('farmer_view_transactions/',views.farmer_view_transactions),
path('farmer_view_scheme/',views.farmer_view_scheme),
path('supplyco_view_transactions/<id>',views.supplyco_view_transactions),
path('user_Send_complaint/',views.user_Send_complaint),
path('user_sendomplaint_post/',views.user_sendomplaint_post),
path('user_view_reply/',views.user_view_reply),
path('ApprovePayment/<id>',views.ApprovePayment),
path('admin_view_reply/',views.admin_view_reply),
path('admin_view_reply_post/',views.admin_view_reply_post),

path('reply/<id>',views.reply),
path('replypost/',views.replypost),
path('forwardtostate/<id>',views.forwardtostate),
path('supplyco_cng_pswrd/',views.supplyco_cng_pswrd),
path('supplyco_cng_pswrd_pst/',views.supplyco_cng_pswrd_pst),
path('stategovernement_scheme/',views.stategovernement_scheme),
path('stategovernemnet_scheme_post/',views.stategovernemnet_scheme_post),
path('state_view_scheme/',views.state_view_scheme),


]
