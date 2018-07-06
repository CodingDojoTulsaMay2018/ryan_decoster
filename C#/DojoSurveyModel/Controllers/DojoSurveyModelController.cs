using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using dojosurveymodel.Models;

namespace dojosurveymodel.Controllers
{
    public class DojoSurveyModelController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        [Route("survey")]
        public IActionResult Survey(string name, string location, string language, string comment) {
            Ninja user = new Ninja() {
                Name = name,
                Location = location,
                Language = language,
                Comment = comment
            };
            return View(user);
        }

        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
