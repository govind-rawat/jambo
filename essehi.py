GRANT SELECT  ON ``new_crownit.ss_%``. * TO 'thakur'@'%'


SELECT CONCAT('GRANT SELECT ON new_crownit.', TABLE_NAME, ' to ''thakur'';') FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'new_crownit' AND TABLE_NAME LIKE 'ss_%'



GRANT SELECT ON new_crownit.ss_atheena_mapping to 'thakur';           
GRANT SELECT ON new_crownit.ss_custom_logic to 'thakur';              
GRANT SELECT ON new_crownit.ss_generic_questions to 'thakur';         
GRANT SELECT ON new_crownit.ss_global_filter_flag to 'thakur';        
GRANT SELECT ON new_crownit.ss_global_flag to 'thakur';               
GRANT SELECT ON new_crownit.ss_image_face to 'thakur';                
GRANT SELECT ON new_crownit.ss_instruction to 'thakur';               
GRANT SELECT ON new_crownit.ss_logics to 'thakur';                    
GRANT SELECT ON new_crownit.ss_operators to 'thakur';                 
GRANT SELECT ON new_crownit.ss_promo_employee_mapping to 'thakur';    
GRANT SELECT ON new_crownit.ss_question_choices to 'thakur';          
GRANT SELECT ON new_crownit.ss_questions to 'thakur';                 
GRANT SELECT ON new_crownit.ss_quota to 'thakur';                     
GRANT SELECT ON new_crownit.ss_scratch_cards to 'thakur';             
GRANT SELECT ON new_crownit.ss_selfie_contest2 to 'thakur';           
GRANT SELECT ON new_crownit.ss_sequence to 'thakur';                  
GRANT SELECT ON new_crownit.ss_survey_ad_info to 'thakur';            
GRANT SELECT ON new_crownit.ss_survey_anaylsis_report to 'thakur';    
GRANT SELECT ON new_crownit.ss_survey_device_info to 'thakur';        
GRANT SELECT ON new_crownit.ss_survey_landing_track to 'thakur';      
GRANT SELECT ON new_crownit.ss_survey_recuiter_map to 'thakur';       
GRANT SELECT ON new_crownit.ss_survey_response_save to 'thakur';      
GRANT SELECT ON new_crownit.ss_survey_responses to 'thakur';          
GRANT SELECT ON new_crownit.ss_survey_user_panel_list to 'thakur';    
GRANT SELECT ON new_crownit.ss_survey_web_auth to 'thakur';           
GRANT SELECT ON new_crownit.ss_surveys to 'thakur';                   
GRANT SELECT ON new_crownit.ss_temp1 to 'thakur';                     
GRANT SELECT ON new_crownit.ss_temp2 to 'thakur';                     
#GRANT SELECT ON new_crownit.ss_temp21 to 'thakur';   \



GRANT SELECT ON new_crownit.survey_conditions to 'thakur';            
GRANT SELECT ON new_crownit.survey_entry to 'thakur';                 
GRANT SELECT ON new_crownit.survey_question_map to 'thakur';          
GRANT SELECT ON new_crownit.survey_questions to 'thakur';             
GRANT SELECT ON new_crownit.survey_response_choice_map to 'thakur';   
GRANT SELECT ON new_crownit.survey_response_choices to 'thakur';      
GRANT SELECT ON new_crownit.survey_response_link_map to 'thakur';     
GRANT SELECT ON new_crownit.survey_response_quota_map to 'thakur';    
GRANT SELECT ON new_crownit.survey_responses to 'thakur';             
GRANT SELECT ON new_crownit.survey_reward_user_map to 'thakur';       
GRANT SELECT ON new_crownit.survey_rewards to 'thakur';               
GRANT SELECT ON new_crownit.surveys to 'thakur'; 
