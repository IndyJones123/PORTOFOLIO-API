import copy
import logging
import traceback
import psycopg2
from MainModuleADM.Logging.logging_config import i_write_log
from MainModuleADM.Utils.validate import i_val as getJsonVal
import mainhttp

mainhttp.loadXml()
logger = logging.getLogger(__name__)

from ListenMain import ListenMain

class ListenExperience(ListenMain):
    def __init__(self, conn: psycopg2.extensions.connection, logger: logging.Logger):
        super().__init__(conn, logger)
        self.logger = logger
        self.conn = conn
        self.cursor = self.conn.cursor()

    def handler(self, path: str, json_req: dict):
        logname = 'fc_auth'
        json_resp = copy.deepcopy(json_req)

        try:
            if path == 'experience':
                rtr = self.experience(json_req)
            elif path == 'project':
                rtr = self.project(json_req)
                
            # elif path == 'check':
            #     rtr = self.get_all_users(json_req)
            else:
                rtr = {
                    'rc': '998',
                    'rcdesc': f'fungsi tidak di kenali: {path}'
                }
        except Exception as ex:
            traceback.print_exc()
            i_write_log(self.logger, logname, f'Error Handling, {ex}')
            json_resp['rc'] = '999'
            json_resp['rcdesc'] = f'general err: {ex}'  
            return json_resp

        return rtr


    def experience(self, json_req: dict) -> dict:
        try:
            logname = "Experience"
            # Query to check if the user exists
            jns = getJsonVal(json_req, 'jns')
            
            if jns is None:
                raise ValueError("The 'jns' key is missing or has no value in the request.")
            
            # Query to check if the user exists
            query = """
                SELECT * FROM experience WHERE jns = %s AND stsrc = 'A'
            """
            
            self.cursor.execute(query, (jns,))
            result = self.cursor.fetchall()
            
            if not result:  # result is None or an empty list
                i_write_log(self.logger, logname, f'Data Experience Tidak Ditemukan')
                return {
                    "status": "not found",
                    "message": "Data Experience Tidak Ditemukan",
                    "data": []  # Optional: return an empty list as the data
                }
            
            # Map column names to values
            column_names = [desc[0] for desc in self.cursor.description]
            data = [dict(zip(column_names, row)) for row in result]
            i_write_log(self.logger, logname, f'Data Experience Ditemukan : {data}')
                        
            return {
                "status": "success",
                "message": "Data Experience Ditemukan",
                "data": data  # Include fetched data if needed
            }
        
        except ValueError as ve:
            return {
                "status": "error",
                "message": str(ve),  # Return the specific validation error message
                "data": None
            }
        except TypeError as te:
            return {
                "status": "error",
                "message": str(te),  # Return the specific type error message
                "data": None
            }
        except Exception as e:
            self.logger.error(f"Error logging in user: {e}")
            return {
                "status": "error",
                "message": "An error occurred while logging in",
                "data": None
            }

    def project(self, json_req: dict) -> dict:
            logname = "Project"
            try:
                
                # Query to check if the user exists
                query = """
                    SELECT * FROM project WHERE stsrc = 'A'
                """
                
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                
                if not result:  # result is None or an empty list
                    i_write_log(self.logger, logname, f'Data Project Tidak Ditemukan')
                    return {
                        "status": "not found",
                        "message": "Data Project Tidak Ditemukan",
                        "data": []  # Optional: return an empty list as the data
                    }
                
                # Map column names to values
                column_names = [desc[0] for desc in self.cursor.description]
                data = [dict(zip(column_names, row)) for row in result]
                i_write_log(self.logger, logname, f'Data Project Ditemukan : {data}')
                
                return {
                    "status": "success",
                    "message": "Data Project Ditemukan",
                    "data": data  # Include fetched data if needed
                }
            
            except ValueError as ve:
                return {
                    "status": "error",
                    "message": str(ve),  # Return the specific validation error message
                    "data": None
                }
            except TypeError as te:
                return {
                    "status": "error",
                    "message": str(te),  # Return the specific type error message
                    "data": None
                }
            except Exception as e:
                self.logger.error(f"Error logging in user: {e}")
                return {
                    "status": "error",
                    "message": "An error occurred while logging in",
                    "data": None
                }
