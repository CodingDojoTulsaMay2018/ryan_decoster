using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using DojoSecrets.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore;

namespace DojoSecrets.Controllers
{
    public class HomeController : Controller
    {
        private YourContext _context;
        public HomeController(YourContext context)
        {
            _context = context;
        }

        [HttpGet]
        [Route("secrets")]
        public IActionResult Secrets()
        {
            if(HttpContext.Session.GetInt32("id") == null) {
                return RedirectToAction("Index", "User");
            }
            DashboardModel view = new DashboardModel()
            {
                Users = new User(),
                Secrets = new Secret(),
                Likes = new Like()
            };
            List<Secret> allSecrets = _context.Secrets
                                        .Include(secret => secret.Likes)
                                            .ThenInclude(like => like.LikedUser)
                                        .ToList();
            int? user_id = HttpContext.Session.GetInt32("id");
            User currentuser = _context.Users.SingleOrDefault(user => user.Id == user_id);
            ViewBag.User = currentuser;
            ViewBag.Secrets = allSecrets.OrderByDescending(secret => secret.Created_At).Take(5);
            return View();
        }

        [HttpPost]
        [Route("PostSecret")]
        public IActionResult PostSecret(Secret secret)
        {
            if(HttpContext.Session.GetInt32("id") == null) {
                return RedirectToAction("Index", "User");
            }
            int? user_id = HttpContext.Session.GetInt32("id");
            User currentuser = _context.Users.SingleOrDefault(user => user.Id == user_id);
            if (ModelState.IsValid) {
                Secret newSecret = new Secret
                {
                    Content = secret.Content,
                    Created_At = DateTime.Now,
                    Updated_At = DateTime.Now,
                    Creator = currentuser,
                    UserId = (int) user_id
                };
                _context.Add(newSecret);
                _context.SaveChanges();
                return RedirectToAction("Secrets");
            }
            TempData["error"] = "Your secret is not valid.";
            return RedirectToAction("Secrets");
        }

        [HttpGet]
        [Route("Delete/{SecretId}")]
        public IActionResult Delete(int SecretId)
        {
            if(HttpContext.Session.GetInt32("id") == null) {
                return RedirectToAction("Index", "User");
            }
            Secret thisSecret = _context.Secrets
                            .Where(secret => secret.Id == SecretId).SingleOrDefault();
            _context.Secrets.Remove(thisSecret);
            _context.SaveChanges();
            return RedirectToAction("Secrets");
        }

        [HttpGet]
        [Route("DeleteMost/{SecretId}")]
        public IActionResult DeleteMost(int SecretId)
        {
            if(HttpContext.Session.GetInt32("id") == null) {
                return RedirectToAction("Index", "User");
            }
            Secret thisSecret = _context.Secrets
                            .Where(secret => secret.Id == SecretId).SingleOrDefault();
            _context.Secrets.Remove(thisSecret);
            _context.SaveChanges();
            return RedirectToAction("MostPopular");
        }

        [HttpGet]
        [Route("Like/{SecretId}")]
        public IActionResult Like(int SecretId)
        {
            if(HttpContext.Session.GetInt32("id") == null) {
                return RedirectToAction("Index", "User");
            }
            int? user_id = HttpContext.Session.GetInt32("id");
            User curruser = _context.Users.Where(user => user.Id == user_id).SingleOrDefault();
            Secret thisSecret = _context.Secrets
                            .Include(secret => secret.Likes)
                                .ThenInclude(g => g.LikedUser)
                            .SingleOrDefault(w => w.Id == SecretId);
            Like newLike = new Like
            {
                UserId = curruser.Id,
                LikedUser = curruser,
                SecretId = thisSecret.Id,
                Secret = thisSecret
            };
            thisSecret.Likes.Add(newLike);
            _context.SaveChanges();
            return RedirectToAction("Secrets");
        }

        [HttpGet]
        [Route("LikeMost/{SecretId}")]
        public IActionResult LikeMost(int SecretId)
        {
            if(HttpContext.Session.GetInt32("id") == null) {
                return RedirectToAction("Index", "User");
            }
            int? user_id = HttpContext.Session.GetInt32("id");
            User curruser = _context.Users.Where(user => user.Id == user_id).SingleOrDefault();
            Secret thisSecret = _context.Secrets
                            .Include(secret => secret.Likes)
                                .ThenInclude(g => g.LikedUser)
                            .SingleOrDefault(w => w.Id == SecretId);
            Like newLike = new Like
            {
                UserId = curruser.Id,
                LikedUser = curruser,
                SecretId = thisSecret.Id,
                Secret = thisSecret
            };
            thisSecret.Likes.Add(newLike);
            _context.SaveChanges();
            return RedirectToAction("MostPopular");
        }

        // [HttpGet]
        // [Route("Unlike/{SecretId}")]
        // public IActionResult Undo(int SecretId)
        // {
        //     if(HttpContext.Session.GetInt32("id") == null) {
        //         return RedirectToAction("Index", "User");
        //     }
        //     int? user_id = HttpContext.Session.GetInt32("id");
        //     User curruser = _context.Users.Where(u => u.Id == user_id).SingleOrDefault();
        //     Secret thisSecret = _context.Secrets
        //                     .Include(secret => secret.Likes)
        //                         .ThenInclude(like => like.LikedUser)
        //                     .SingleOrDefault(w => w.Id == SecretId);
        //     Like thisLike = _context.Likes.Where(user => user.UserId == user_id).Where(secret => secret.SecretId == SecretId).SingleOrDefault();
        //     thisSecret.Likes.Remove(thisLike);
        //     _context.SaveChanges();
        //     return RedirectToAction("Secrets");
        // }

        [HttpGet]
        [Route("mostpopular")]
        public IActionResult MostPopular()
        {
            if(HttpContext.Session.GetInt32("id") == null) {
                return RedirectToAction("Index", "User");
            }
            DashboardModel view = new DashboardModel()
            {
                Users = new User(),
                Secrets = new Secret(),
                Likes = new Like()
            };
            List<Secret> allSecrets = _context.Secrets
                                        .Include(secret => secret.Likes)
                                            .ThenInclude(like => like.LikedUser)
                                        .ToList();
            int? user_id = HttpContext.Session.GetInt32("id");
            User currentuser = _context.Users.SingleOrDefault(user => user.Id == user_id);
            ViewBag.User = currentuser;
            ViewBag.Secrets = allSecrets.OrderByDescending(secret => secret.Likes.Count);
            return View("MostPopular");
        }
    }
}
